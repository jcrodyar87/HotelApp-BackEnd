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

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/clients",tags=["Clients"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.ClientWithCountry])
async def show_clients(country_id: str = '', status: str = '', text: str = '', db: Session = Depends(get_db)):
    clients = db.query(models.Client)
    if status != '':
        clients = clients.filter(models.Client.status == status)
    if country_id !='':
        clients = clients.filter(models.Client.country_id == country_id)
    if text != '':
        clients = clients.filter(
            or_(
                models.Client.firstname.like('%'+text+'%'), 
                models.Client.lastname.like('%'+text+'%'), 
                models.Client.document.like('%'+text+'%'), 
                models.Client.phone.like('%'+text+'%'), 
                models.Client.email.like('%'+text+'%')
            ))
    clients = clients.filter(models.Client.status != 3).order_by(models.Client.firstname.asc()).all()
    return clients

@router.get("/{id}",response_model=schemas.ClientFull)
async def show_client(id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter_by(id=id).first()
    return client

@router.post("/",response_model=schemas.ClientFull)
async def create_client(client_params: schemas.Client, db: Session=Depends(get_db)):
    client = models.Client(
        firstname = client_params.firstname,
        lastname = client_params.lastname, 
        document = client_params.document, 
        phone = client_params.phone, 
        email = client_params.email, 
        status = client_params.status,
        reservations_quantity = 0,
        country_id = client_params.country_id
        )
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.put("/{id}")
async def update_client(id: int, client_params: schemas.ClientUpdate, db: Session=Depends(get_db)):
    client = db.query(models.Client).filter_by(id=id).first()
    prev_reservation = db.query(models.Reservation).filter(models.Reservation.client_id==id).filter(models.Reservation.status != 3).first()
    if client_params.status == 0 and prev_reservation is not None:
        raise HTTPException(status_code=400, detail="No se puede desactivar el cliente porque tiene una reserva activa")
    else:
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
    client.status = 3
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response

@router.get("/download-excel/",status_code=200)
async def download_excel(country_id: str = '', status: str = '', text: str = '', db: Session=Depends(get_db)):
    file_name = f'static/files/clients.xlsx'
    wb = Workbook()
    ws = wb.active
    clients = db.query(models.Client)
    if status != '':
        clients = clients.filter(models.Client.status == status)
    if country_id !='':
        clients = clients.filter(models.Client.country_id == country_id)
    if text != '':
        clients = clients.filter(
            or_(
                models.Client.firstname.like('%'+text+'%'), 
                models.Client.lastname.like('%'+text+'%'), 
                models.Client.document.like('%'+text+'%'), 
                models.Client.phone.like('%'+text+'%'), 
                models.Client.email.like('%'+text+'%')
            ))
    clients = clients.filter(models.Client.status != 3).order_by(models.Client.firstname.asc()).all()
    ws.append([
                'Cliente', 
                'Documento', 
                'Teléfono', 
                'Email', 
                'País',
                'N° de Reservas',
                'Última Reserva',
                'Fecha de Creación',
                'Estado'
            ])
    for client in clients:
        ws.append([
                    client.firstname + ' ' + client.lastname,client.document, 
                    client.phone, 
                    client.email, 
                    client.country.name, 
                    client.reservations_quantity, 
                    client.last_reservation, 
                    client.created_date, 
                    client.status
                ])
    wb.save(file_name)
    
    file_path = Path(file_name)
    if file_path.is_file():
        return {"detail": 'http://127.0.0.1:8000/' + file_name}
    else:
        raise HTTPException(status_code=400, detail="No se ha podido generar el excel de los clientes")