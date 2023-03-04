from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/room-types",tags=["Room Types"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/",response_model=List[schemas.RoomType])
async def show_room_types(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    room_types = db.query(models.RoomType).filter(models.RoomType.status != 3).all()
    return room_types

@router.get("/{id}",response_model=schemas.RoomType)
async def show_room_type(id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    room_type = db.query(models.RoomType).filter_by(id=id).first()
    return room_type

@router.post("/",response_model=schemas.RoomType)
async def create_room_type(room_type_params: schemas.RoomType, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    room_type = models.RoomType(
        name = room_type_params.name,
        status = room_type_params.status
    )
    db.add(room_type)
    db.commit()
    db.refresh(room_type)
    return room_type

@router.put("/{id}",response_model=schemas.RoomType)
async def update_room_type(id: int, room_type_params: schemas.RoomTypeUpdate, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    room_type = db.query(models.RoomType).filter_by(id=id).first()
    room_type.name = room_type_params.name
    room_type.status = room_type_params.status
    room_type.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(room_type)
    return room_type

@router.delete("/{id}",response_model=schemas.Response)
async def delete_room_type(id: int, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    room_type = db.query(models.RoomType).filter_by(id=id).first()
    room_type.status = 3
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
