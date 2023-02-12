from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/closed-schedules",tags=["Closed Schedules"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.ClosedSchedule])
async def show_closed_schedules(db: Session = Depends(get_db)):
    closed_schedules = db.query(models.ClosedSchedule).all()
    return closed_schedules

@router.get("/{id}",response_model=schemas.ClosedSchedule)
async def show_closed_schedule(id: int, db: Session = Depends(get_db)):
    closed_schedule = db.query(models.ClosedSchedule).filter_by(id=id).first()
    return closed_schedule

@router.post("/",response_model=schemas.ClosedSchedule)
async def create_closed_schedule(country_params: schemas.ClosedSchedule, db: Session=Depends(get_db)):
    closed_schedule = models.ClosedSchedule(
        start_date = country_params.start_date,
        end_date = country_params.end_date, 
        description = country_params.description,
        status = country_params.status,
        room_id = country_params.room_id,
        )
    db.add(closed_schedule)
    db.commit()
    db.refresh(closed_schedule)
    return closed_schedule

@router.put("/{id}",response_model=schemas.ClosedSchedule)
async def update_closed_schedule(id: int, country_params: schemas.ClosedScheduleUpdate, db: Session=Depends(get_db)):
    closed_schedule = db.query(models.ClosedSchedule).filter_by(id=id).first()
    closed_schedule.start_date = country_params.start_date
    closed_schedule.end_date = country_params.end_date
    closed_schedule.description = country_params.description
    closed_schedule.status = country_params.status
    closed_schedule.room_id = country_params.room_id
    closed_schedule.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(closed_schedule)
    return closed_schedule

@router.delete("/{id}",response_model=schemas.Response)
async def delete_closed_schedule(id: int, db: Session=Depends(get_db)):
    closed_schedule = db.query(models.ClosedSchedule).filter_by(id=id).first()
    db.delete(closed_schedule)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
