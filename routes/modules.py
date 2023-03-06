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

router = APIRouter(prefix="/modules",tags=["Modules"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/")
async def show_modules(token: str = Depends(oauth2_scheme)):
    modules = [ 
            { "id": "calendar","name": "Disponibilidad"},
            { "id": "clients","name": "Clientes"},
            { "id": "rooms","name": "Habitaciones"},
            { "id": "users","name": "Usuarios"},
            { "id": "roles","name": "Roles"}
            ]
    return modules