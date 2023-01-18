from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/reservations",tags=["Reservations"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/",response_model=List[schemas.ReservationWithClientAndRoom])
async def show_reservations(db: Session = Depends(get_db)):
    reservations = db.query(models.Reservation).all()
    return reservations

@router.get("/{id}",response_model=schemas.ReservationWithClientAndRoom)
async def show_reservation(id: int, db: Session = Depends(get_db)):
    reservation = db.query(models.Reservation).filter_by(id=id).first()
    return reservation

@router.post("/",response_model=schemas.Reservation)
async def create_reservation(reservation_params: schemas.Reservation, db: Session=Depends(get_db)):
    reservation = models.Reservation(
        checkin = reservation_params.checkin, 
        checkout = reservation_params.checkout, 
        total = reservation_params.total, 
        done_payment = reservation_params.done_payment, 
        pending_payment = reservation_params.pending_payment,
        status = reservation_params.status,
        client_id = reservation_params.client_id,
        room_id = reservation_params.room_id
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

@router.put("/{id}",response_model=schemas.Reservation)
async def update_reservation(id: int, reservation_params: schemas.ReservationUpdate, db: Session=Depends(get_db)):
    reservation = db.query(models.Reservation).filter_by(id=id).first()
    reservation.checkin = reservation_params.checkin, 
    reservation.checkout = reservation_params.checkout, 
    reservation.total = reservation_params.total, 
    reservation.done_payment = reservation_params.done_payment, 
    reservation.pending_payment = reservation_params.pending_payment,
    reservation.status = reservation_params.status,
    reservation.client_id = reservation_params.client_id,
    reservation.room_id = reservation_params.room_id
    reservation.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(reservation)
    return reservation

@router.delete("/{id}",response_model=schemas.Response)
async def delete_reservation(id: int, db: Session=Depends(get_db)):
    reservation = db.query(models.Reservation).filter_by(id=id).first()
    db.delete(reservation)
    db.commit()
    response = schemas.Response(message="Eliminado exitosamente")
    return response