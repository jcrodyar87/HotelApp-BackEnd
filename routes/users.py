from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy import or_
from pathlib import Path
from openpyxl import Workbook
from fastapi.security import OAuth2PasswordBearer

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users",tags=["Users"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.get("/",response_model=List[schemas.UserWithRole], response_model_exclude={'password','token'})
async def show_users(role_id: str = '', status: str = '', text: str = '', token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    users = db.query(models.User)
    if status != '':
        users = users.filter(models.User.status == status)
    if role_id !='':
        users = users.filter(models.User.role_id == role_id)
    if text != '':
        users = users.filter(
            or_(
                models.User.firstname.like('%'+text+'%'), 
                models.User.lastname.like('%'+text+'%'), 
                models.User.username.like('%'+text+'%')
            ))
    users = users.filter(models.User.status != 3).order_by(models.User.username.asc()).all()
    return users

@router.get("/{id}",response_model=schemas.User, response_model_exclude={'password','token'})
async def show_user(id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(id=id).first()
    return user

@router.post("/",response_model=schemas.User, response_model_exclude={'password','token'})
async def create_user(user_params: schemas.User, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    user = models.User(
        username = user_params.username,
        firstname = user_params.firstname,
        lastname = user_params.lastname,
        password = get_password_hash(user_params.password),
        status = user_params.status,
        role_id = user_params.role_id
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/{id}",response_model=schemas.User, response_model_exclude={'password','token'})
async def update_user(id: int, user_params: schemas.UserUpdate, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    user = db.query(models.User).filter_by(id=id).first()
    user.username = user_params.username
    user.firstname = user_params.firstname
    user.lastname = user_params.lastname
#    user.password =  get_password_hash(user_params.password)
    user.status = user_params.status
    user.role_id = user_params.role_id
    user.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{id}",response_model=schemas.Response)
async def delete_user(id: int, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    user = db.query(models.User).filter_by(id=id).first()
    user.status = 3
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response

@router.get("/download-excel/",status_code=200)
async def download_excel(db: Session=Depends(get_db)):
    file_name = f'static/files/users.xlsx'
    wb = Workbook()
    ws = wb.active
    users = db.query(models.User).filter(models.User.status != 3).all()
    ws.append([
                'Nombre de usuario', 
                'Nombre', 
                'Apellido',
                'Rol',
                'Fecha de Creación',
                'Estado'
            ])
    for user in users:
        ws.append([
                    user.username, 
                    user.firstname,
                    user.lastname,
                    user.role.name, 
                    user.created_date, 
                    user.status
                ])
    wb.save(file_name)
    
    file_path = Path(file_name)
    if file_path.is_file():
        return {"detail": 'http://127.0.0.1:8000/' + file_name}
    else:
        raise HTTPException(status_code=400, detail="No se ha podido generar el excel de los roles")