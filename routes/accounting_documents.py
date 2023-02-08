from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/accounting-documents",tags=["Accounting Documents"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.AccountingDocument])
async def show_accounting_documents(reservation_id: str = '',db: Session = Depends(get_db)):
    if reservation_id == '':
        accounting_documents = db.query(models.AccountingDocument).all()
    else:
        accounting_documents = db.query(models.AccountingDocument).filter(models.AccountingDocument.reservation_id == reservation_id).all()
    return accounting_documents

@router.get("/{id}",response_model=schemas.AccountingDocument)
async def show_accounting_document(id: int, db: Session = Depends(get_db)):
    accounting_document = db.query(models.AccountingDocument).filter_by(id=id).first()
    return accounting_document

@router.post("/",response_model=schemas.AccountingDocument)
async def create_accounting_document(accounting_document_params: schemas.AccountingDocument, db: Session=Depends(get_db)):
    accounting_document = models.AccountingDocument(
        number = accounting_document_params.number,
        client_number = accounting_document_params.client_number, 
        client_name = accounting_document_params.client_name,
        client_address = accounting_document_params.client_address,
        issue_date = accounting_document_params.issue_date,
        type = accounting_document_params.type,
        currency_type = accounting_document_params.currency_type,
        total_sale = accounting_document_params.total_sale,
        tax = accounting_document_params.tax,
        total = accounting_document_params.total,
        status = accounting_document_params.status,
        reservation_id = accounting_document_params.reservation_id,
    )
    
    db.add(accounting_document)
    db.commit()
    db.refresh(accounting_document)
    return accounting_document

@router.put("/{id}",response_model=schemas.AccountingDocument)
async def update_accounting_document(id: int, accounting_document_params: schemas.CountryUpdate, db: Session=Depends(get_db)):
    accounting_document = db.query(models.AccountingDocument).filter_by(id=id).first()

    accounting_document.number = accounting_document_params.number
    accounting_document.client_number = accounting_document_params.client_number
    accounting_document.client_name = accounting_document_params.client_name
    accounting_document.client_address = accounting_document_params.client_address
    accounting_document.issue_date = accounting_document_params.issue_date
    accounting_document.type = accounting_document_params.type
    accounting_document.currency_type = accounting_document_params.currency_type
    accounting_document.total_sale = accounting_document_params.total_sale
    accounting_document.tax = accounting_document_params.tax
    accounting_document.total = accounting_document_params.total
    accounting_document.status = accounting_document_params.status
    accounting_document.reservation_id = accounting_document_params.reservation_id
    accounting_document.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(accounting_document)
    return accounting_document

@router.delete("/{id}",response_model=schemas.Response)
async def delete_country(id: int, db: Session=Depends(get_db)):
    accounting_document = db.query(models.AccountingDocument).filter_by(id=id).first()
    db.delete(accounting_document)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
