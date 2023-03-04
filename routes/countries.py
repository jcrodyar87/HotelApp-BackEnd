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

router = APIRouter(prefix="/countries",tags=["Countries"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/",response_model=List[schemas.Country])
async def show_countries(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    countries = db.query(models.Country).filter(models.Country.status != 3).all()
    return countries

@router.get("/{id}",response_model=schemas.Country)
async def show_country(id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    country = db.query(models.Country).filter_by(id=id).first()
    return country

@router.post("/",response_model=schemas.Country)
async def create_country(country_params: schemas.Country, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    country = models.Country(
        name = country_params.name,
        alpha3 = country_params.alpha3, 
        status = country_params.status
        )
    db.add(country)
    db.commit()
    db.refresh(country)
    return country

@router.put("/{id}",response_model=schemas.Country)
async def update_country(id: int, country_params: schemas.CountryUpdate, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    country = db.query(models.Country).filter_by(id=id).first()
    country.name = country_params.name
    country.alpha3 = country_params.alpha3
    country.status = country_params.status
    country.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(country)
    return country

@router.delete("/{id}",response_model=schemas.Response)
async def delete_country(id: int, token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    country = db.query(models.Country).filter_by(id=id).first()
    country.status = 3
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
