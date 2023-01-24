from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/clients",tags=["Clients"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.Client])
async def show_clients(db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return clients

@router.get("/{id}",response_model=schemas.Client)
async def show_client(id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter_by(id=id).first()
    return client

@router.post("/",response_model=schemas.Client)
async def create_client(client_params: schemas.Client, db: Session=Depends(get_db)):
    client = models.Client(
        firstname = client_params.firstname,
        lastname = client_params.lastname, 
        document = client_params.document, 
        phone = client_params.phone, 
        email = client_params.email, 
        status = client_params.status,
        country_id = client_params.country_id
        )
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.put("/{id}",response_model=schemas.Client)
async def update_client(id: int, client_params: schemas.ClientUpdate, db: Session=Depends(get_db)):
    client = db.query(models.Client).filter_by(id=id).first()
    client.firstname = client_params.firstname
    client.lastname = client_params.lastname
    client.document = client_params.document
    client.phone = client_params.phone
    client.email = client_params.email
    client.status = client_params.status
    client.country_id = client_params.country_id
    client.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(client)
    return client

@router.delete("/{id}",response_model=schemas.Response)
async def delete_client(id: int, db: Session=Depends(get_db)):
    client = db.query(models.Client).filter_by(id=id).first()
    db.delete(client)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
