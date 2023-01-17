from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users",tags=["users"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.User])
async def show_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post("/",response_model=schemas.User)
async def create_user(user_params: schemas.User, db: Session=Depends(get_db)):
    user = models.User(
        username = user_params.username,
        status = user_params.status
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/{id}",response_model=schemas.User)
async def update_user(id: int, user_params: schemas.UserUpdate, db: Session=Depends(get_db)):
    user = db.query(models.User).filter_by(id=id).first()
    user.username = user_params.username
    user.status = user_params.status
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{id}",response_model=schemas.Response)
async def delete_user(id: int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter_by(id=id).first()
    db.delete(user)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
