from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users",tags=["Users"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.get("/",response_model=List[schemas.User])
async def show_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post("/",response_model=schemas.User)
async def create_user(user_params: schemas.User, db: Session=Depends(get_db)):
    user = models.User(
        username = user_params.username,
        firstname = user_params.firstname,
        lastname = user_params.lastname,
        password = get_password_hash(user_params.password),
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
    user.firstname = user_params.firstname
    user.lastname = user_params.lastname
    user.password = user_params.password
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
