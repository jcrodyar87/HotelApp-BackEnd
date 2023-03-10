from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import or_
from pathlib import Path
from openpyxl import Workbook
from fastapi.security import OAuth2PasswordBearer

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/rooms",tags=["Rooms"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/",response_model=List[schemas.RoomWithRoomType])
async def show_rooms(type_id: str = '', status: str = '', text: str = '', token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    rooms = db.query(models.Room)
    if status != '':
        rooms = rooms.filter(models.Room.status == status)
    if type_id !='':
        rooms = rooms.filter(models.Room.room_type_id == type_id)
    if text != '':
        rooms = rooms.filter(
            or_(
                models.Room.name.like('%'+text+'%'), 
                models.Room.description.like('%'+text+'%')
            ))
    rooms = rooms.filter(models.Room.status != 3).order_by(models.Room.name.asc()).all()
    return rooms

@router.get("/{id}",response_model=schemas.Room)
async def show_room(id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    room = db.query(models.Room).filter_by(id=id).first()
    return room

@router.post("/",response_model=schemas.Room)
async def create_room(room_params: schemas.Room, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    room = models.Room(
        name = room_params.name, 
        description = room_params.description, 
        price = room_params.price, 
        capacity = room_params.capacity,
        room_type_id = room_params.room_type_id, 
        status = room_params.status
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

@router.put("/{id}")
async def update_room(id: int, room_params: schemas.RoomUpdate, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    prev_reservation = db.query(models.Reservation).filter(models.Reservation.room_id==id).first()
    if room_params.status == 0 and prev_reservation is not None:
        raise HTTPException(status_code=400, detail="No se puede desactivar la habitación porque tiene una reserva activa")
    else:
        room = db.query(models.Room).filter_by(id=id).first()
        room.name = room_params.name
        room.description = room_params.description
        room.price = room_params.price
        room.capacity = room_params.capacity
        room.room_type_id = room_params.room_type_id
        room.status = room_params.status
        room.updated_date = datetime.utcnow()
        db.commit()
        db.refresh(room)
        return room

@router.delete("/{id}",response_model=schemas.Response)
async def delete_room(id: int, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    room = db.query(models.Room).filter_by(id=id).first()
    room.status = 3
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response

@router.get("/download-excel/",status_code=200)
async def download_excel(db: Session=Depends(get_db)):
    file_name = f'static/files/rooms.xlsx'
    wb = Workbook()
    ws = wb.active
    rooms = db.query(models.Room).filter(models.Room.status != 3).all()
    ws.append([
                'Nombre', 
                'Descripción', 
                'Precio', 
                'Capacidad', 
                'Tipo',
                'Fecha de Creación',
                'Estado'
            ])
    for room in rooms:
        ws.append([
                    room.name, 
                    room.description, 
                    room.price, 
                    room.capacity, 
                    room.room_type.name, 
                    room.created_date, 
                    room.status
                ])
    wb.save(file_name)
    
    file_path = Path(file_name)
    if file_path.is_file():
        return {"detail": 'http://127.0.0.1:8000/' + file_name}
    else:
        raise HTTPException(status_code=400, detail="No se ha podido generar el excel de las habitaciones")