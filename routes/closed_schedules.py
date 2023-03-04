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

@router.get("/",response_model=List[schemas.ClosedScheduleWithRoom])
async def show_closed_schedules(db: Session = Depends(get_db)):
    closed_schedules = db.query(models.ClosedSchedule).filter(models.ClosedSchedule.status != 3).all()
    return closed_schedules

@router.get("/{id}",response_model=schemas.ClosedScheduleWithRoom)
async def show_closed_schedule(id: int, db: Session = Depends(get_db)):
    closed_schedule = db.query(models.ClosedSchedule).filter_by(id=id).first()
    return closed_schedule

@router.post("/")
async def create_closed_schedule(closed_schedule_params: schemas.ClosedSchedule, db: Session=Depends(get_db)):
    prev_reservation = db.query(models.Reservation).filter(models.Reservation.checkin ==closed_schedule_params.start_date ).\
        filter(models.Reservation.room_id.in_(closed_schedule_params.rooms)).filter(models.Reservation.status != 3).first()
    if prev_reservation is not None:
        raise HTTPException(status_code=400, detail="No se puede cerrar ese horario y habitación porque existen reservas activas")
    else:
        for room in closed_schedule_params.rooms:
            closed_schedule = models.ClosedSchedule(
                start_date = closed_schedule_params.start_date,
                end_date = closed_schedule_params.end_date, 
                description = closed_schedule_params.description,
                status = closed_schedule_params.status,
                room_id = room,
                )
            db.add(closed_schedule)
            db.commit()
            db.refresh(closed_schedule)
        return closed_schedule

@router.put("/{id}",response_model=schemas.ClosedScheduleWithRoom)
async def update_closed_schedule(id: int, closed_schedule_params: schemas.ClosedScheduleUpdate, db: Session=Depends(get_db)):
    closed_schedule = db.query(models.ClosedSchedule).filter_by(id=id).first()
    closed_schedule.start_date = closed_schedule_params.start_date
    closed_schedule.end_date = closed_schedule_params.end_date
    closed_schedule.description = closed_schedule_params.description
    closed_schedule.status = closed_schedule_params.status
    closed_schedule.room_id = closed_schedule_params.room_id
    closed_schedule.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(closed_schedule)
    return closed_schedule

@router.delete("/{id}",response_model=schemas.Response)
async def delete_closed_schedule(id: int, db: Session=Depends(get_db)):
    closed_schedule = db.query(models.ClosedSchedule).filter_by(id=id).first()
    closed_schedule.status = 3
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response
