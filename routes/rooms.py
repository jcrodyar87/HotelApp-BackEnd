from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/rooms",tags=["Rooms"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.RoomWithRoomType])
async def show_rooms(db: Session = Depends(get_db)):
    rooms = db.query(models.Room).all()
    return rooms

@router.get("/{id}",response_model=schemas.Room)
async def show_room(id: int, db: Session = Depends(get_db)):
    room = db.query(models.Room).filter_by(id=id).first()
    return room

@router.post("/",response_model=schemas.Room)
async def create_room(room_params: schemas.Room, db: Session=Depends(get_db)):
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

@router.put("/{id}",response_model=schemas.Room)
async def update_room(id: int, room_params: schemas.RoomUpdate, db: Session=Depends(get_db)):
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
async def delete_room(id: int, db: Session=Depends(get_db)):
    room = db.query(models.Room).filter_by(id=id).first()
    db.delete(room)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response