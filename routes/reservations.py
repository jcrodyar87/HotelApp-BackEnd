from typing import List
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/reservations",tags=["Reservations"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

conf = ConnectionConfig(
    MAIL_USERNAME =  "7fa57049544924",
    MAIL_PASSWORD = "9bc9810468b2ff",
    MAIL_FROM = "contact@hotelapp.com",
    MAIL_PORT=587,
    MAIL_SERVER= "smtp.mailtrap.io",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

@router.get("/",response_model=List[schemas.ReservationWithClientAndRoom])
async def show_reservations(start_date: str = '', end_date: str = '', db: Session = Depends(get_db)):
    if start_date == '' and end_date == '':
        reservations = db.query(models.Reservation).order_by(models.Reservation.checkin.asc()).all()
    else:
        reservations = db.query(models.Reservation).filter(models.Reservation.checkin <= end_date).\
        filter(models.Reservation.checkin >= start_date).order_by(models.Reservation.checkin.asc()).all()
    return reservations

@router.get("/{id}",response_model=schemas.ReservationWithClientAndRoom)
async def show_reservation(id: int, db: Session = Depends(get_db)):
    reservation = db.query(models.Reservation).filter_by(id=id).first()
    return reservation

@router.get("/{id}/accounting-document/")
async def show_reservation_accounting_document(id: int, db: Session = Depends(get_db)):
    accounting_document = db.query(models.AccountingDocument).filter_by(reservation_id=id).first()
    if accounting_document is None:
        return {"detail": "La reserva no tiene un pago registrado"}
    else: 
        return accounting_document

@router.post("/")
async def create_reservation(reservation_params: schemas.Reservation, db: Session=Depends(get_db)):
    prev_reservation = db.query(models.Reservation).filter(models.Reservation.checkin ==reservation_params.checkin ).\
        filter(models.Reservation.room_id == reservation_params.room_id).first()
    if prev_reservation is not None:
        raise HTTPException(status_code=400, detail="Ya existe una reserva para ese horario y habitación")
    else:
        prev_closed_schedule = db.query(models.ClosedSchedule).filter(models.ClosedSchedule.start_date == reservation_params.checkin ).\
        filter(models.ClosedSchedule.room_id == reservation_params.room_id).first()
        if prev_closed_schedule is not None:
            raise HTTPException(status_code=400, detail="El horario elegido no recibe reservas porque está bloqueado - " + prev_closed_schedule.description)
        else:
            reservation = models.Reservation(
                checkin = reservation_params.checkin, 
                checkout = reservation_params.checkout, 
                adults = reservation_params.adults,
                children = reservation_params.children,
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

@router.put("/{id}")
async def update_reservation(id: int, reservation_params: schemas.ReservationUpdate, db: Session=Depends(get_db)):
    prev_reservation = db.query(models.Reservation).filter(models.Reservation.checkin ==reservation_params.checkin ).\
        filter(models.Reservation.room_id == reservation_params.room_id).\
        filter(models.Reservation.id != id).first()
    if prev_reservation is not None:
        raise HTTPException(status_code=400, detail="Ya existe una reserva para ese horario y habitación")
    else:
        prev_closed_schedule = db.query(models.ClosedSchedule).filter(models.ClosedSchedule.start_date == reservation_params.checkin ).\
        filter(models.ClosedSchedule.room_id == reservation_params.room_id).first()
        if prev_closed_schedule is not None:
            raise HTTPException(status_code=400, detail="El horario elegido no recibe reservas porque está bloqueado - " + prev_closed_schedule.description)
        else:
            reservation = db.query(models.Reservation).filter_by(id=id).first()
            reservation.checkin = reservation_params.checkin
            reservation.checkout = reservation_params.checkout  
            reservation.adults = reservation_params.adults
            reservation.children = reservation_params.children
            reservation.total = reservation_params.total
            reservation.done_payment = reservation_params.done_payment
            reservation.pending_payment = reservation_params.pending_payment
            reservation.status = reservation_params.status
            reservation.client_id = reservation_params.client_id
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

@router.post("/send-email/",status_code=200)
async def send_reservation_email(reservation_params: schemas.ReservationEmail, db: Session=Depends(get_db)):
    reservation = db.query(models.Reservation).filter_by(id=reservation_params.id).first()
    if reservation is None:
        raise HTTPException(status_code=400, detail="No se ha podido enviar el email con el detalle de la reserva")
    html = f"""
    <p><img style="position:relative;left:33.3%;width:200px" src="http://137.184.29.255/static/img/logo.jpg"></p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 500;line-height: 32px;text-align: center;">HOTEL LAS PALMERAS DE HUANCHACO<p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 22px;text-align: center;">Av. Larco 1624 - Sector Los Tumbos – Huanchaco</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 22px;text-align: center;">Teléfono: 924284185 - (044) 46 11 99</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;">Hola, { reservation.client.firstname} has realizado una reserva</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Nombre del cliente: </b>{reservation.client.firstname}  {reservation.client.lastname}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Documento:</b> {reservation.client.document}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Teléfono:</b> {reservation.client.phone}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Su reserva:</b> {reservation.room.name} - {reservation.room.room_type.name}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;">{reservation.room.description}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Clientes:</b> {reservation.adults} Adulto(s), {reservation.children} Niño(s)</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Llegada:</b> {reservation.checkin.strftime('%d/%m/%Y')}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Salida:</b> {reservation.checkout.strftime('%d/%m/%Y')}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Hora de llegada:</b> { reservation.checkin.strftime('%d/%m/%Y')}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Costo total:</b> S/{ reservation.total:,.2f}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Total pagado:</b> S/{reservation.done_payment:,.2f}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: left;"><b>Queda por pagar:</b> S/{reservation.pending_payment:,.2f}</p>
    <p style="padding: 10px 20px;font-size: 16px;font-weight: 400;line-height: 24px;text-align: center;">Gracias por su reserva, lo esperamos pronto</p>
    """
    message = MessageSchema(
        subject="HotelApp - Has realizado una reserva",
        recipients=[reservation.client.email],
        body=html,
        subtype="html")

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"detail": "Se ha enviado un email con el detalle de la reserva"}