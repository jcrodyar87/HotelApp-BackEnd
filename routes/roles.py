from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/roles",tags=["Roles"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.Role])
async def show_roles(db: Session = Depends(get_db)):
    roles = db.query(models.Role).all()
    return roles

@router.get("/{id}",response_model=schemas.Role)
async def show_role(id: int, db: Session = Depends(get_db)):
    role = db.query(models.Role).filter_by(id=id).first()
    return role

@router.post("/",response_model=schemas.Role)
async def create_role(role_params: schemas.Role, db: Session=Depends(get_db)):
    role = models.Role(
        name = role_params.name,
        modules = role_params.modules, 
        status = role_params.status
    )
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

@router.put("/{id}",response_model=schemas.Role)
async def update_role(id: int, role_params: schemas.RoleUpdate, db: Session=Depends(get_db)):
    role = db.query(models.Role).filter_by(id=id).first()
    role.name = role_params.name
    role.modules = role_params.modules
    role.status = role_params.status
    role.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(role)
    return role

@router.delete("/{id}",response_model=schemas.Response)
async def delete_role(id: int, db: Session=Depends(get_db)):
    role = db.query(models.Role).filter_by(id=id).first()
    db.delete(role)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
