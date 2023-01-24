from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/room-types",tags=["Room Types"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.RoomType])
async def show_room_types(db: Session = Depends(get_db)):
    room_types = db.query(models.RoomType).all()
    return room_types

@router.get("/{id}",response_model=schemas.RoomType)
async def show_room_type(id: int, db: Session = Depends(get_db)):
    room_type = db.query(models.RoomType).filter_by(id=id).first()
    return room_type

@router.post("/",response_model=schemas.RoomType)
async def create_room_type(room_type_params: schemas.RoomType, db: Session=Depends(get_db)):
    room_type = models.RoomType(
        name = room_type_params.name,
        status = room_type_params.status
    )
    db.add(room_type)
    db.commit()
    db.refresh(room_type)
    return room_type

@router.put("/{id}",response_model=schemas.RoomType)
async def update_room_type(id: int, room_type_params: schemas.RoomTypeUpdate, db: Session=Depends(get_db)):
    room_type = db.query(models.RoomType).filter_by(id=id).first()
    room_type.name = room_type_params.name
    room_type.status = room_type_params.status
    room_type.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(room_type)
    return room_type

@router.delete("/{id}",response_model=schemas.Response)
async def delete_room_type(id: int, db: Session=Depends(get_db)):
    room_type = db.query(models.RoomType).filter_by(id=id).first()
    db.delete(room_type)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
