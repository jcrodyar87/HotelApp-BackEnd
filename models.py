from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime, Date
from config.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    modules = Column(Text())
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200))
    firstname = Column(String(250))
    lastname = Column(String(250))
    password = Column(String(250))
    status = Column(Integer)
    token = Column(String(250), default=None)
    role_id = Column(Integer, ForeignKey("role.id"))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role", back_populates="user")

    
class RoomType(Base):
    __tablename__ = "room_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    room = relationship("Room", back_populates="room_type")

    
class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    description = Column(Text())
    price = Column(Numeric())
    capacity = Column(Integer)
    status = Column(Integer)
    room_type_id = Column(Integer, ForeignKey("room_type.id"))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    room_type = relationship("RoomType", back_populates="room")
    reservation = relationship("Reservation", back_populates="room")
    closed_schedule = relationship("ClosedSchedule", back_populates="room")


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    alpha3 = Column(String(3))
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    client = relationship("Client", back_populates="country")

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    document = Column(String(100))
    phone = Column(String(100))
    email = Column(String(150))
    reservations_quantity = Column(Integer, default=0)
    last_reservation = Column(DateTime, default=datetime.utcnow)
    status = Column(Integer)
    country_id = Column(Integer, ForeignKey("country.id"))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    country = relationship("Country", back_populates="client")
    reservation = relationship("Reservation", back_populates="client")

class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True)
    checkin = Column(Date)
    checkout = Column(Date)
    adults = Column(Integer)
    children = Column(Integer)
    subtotal = Column(Numeric())
    additional_amount = Column(Numeric())
    observations = Column(Text())
    total = Column(Numeric())
    done_payment = Column(Numeric())
    pending_payment = Column(Numeric())
    status = Column(Integer, default=1)
    client_id = Column(Integer, ForeignKey("client.id"))
    room_id = Column(Integer, ForeignKey("room.id"))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    client = relationship("Client", back_populates="reservation")
    room = relationship("Room", back_populates="reservation")
    #accounting_document = relationship("AccountingDocument", back_populates="reservation")

class AccountingDocument(Base):
    __tablename__ = "accounting_document"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(200))
    client_number = Column(String(100))
    client_name = Column(String(300))
    client_address = Column(String(300))
    issue_date = Column(Date)
    type = Column(Integer())
    currency_type = Column(Integer())
    total_sale =  Column(Numeric())
    tax =  Column(Numeric())
    total =  Column(Numeric())
    status = Column(Integer, default=1)
    reservation_id = Column(Integer, ForeignKey("reservation.id"))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    #reservation = relationship("Reservation", back_populates="accounting_document")

class ClosedSchedule(Base):
    __tablename__ = "closed_schedule"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String(350))
    status = Column(Integer, default=1)
    room_id = Column(Integer, ForeignKey("room.id"))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

    room = relationship("Room", back_populates="closed_schedule")