from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime, Date
from config.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, date

class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    description = Column(Text())
    type = Column(String(150))
    price = Column(Numeric())
    capacity = Column(Integer)
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    reservation = relationship("Reservation", back_populates="room")

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    document = Column(String(100))
    phone = Column(String(100))
    email = Column(String(150))
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    reservation = relationship("Reservation", back_populates="client")

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    modules = Column(Text())
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200))
    firstname = Column(String(250))
    lastname = Column(String(250))
    password = Column(String(250))
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("role.id"))

    role = relationship("Role", back_populates="user")

class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True)
    checkin = Column(Date)
    checkout = Column(Date)
    total = Column(Numeric())
    done_payment = Column(Numeric())
    pending_payment = Column(Numeric())
    status = Column(Integer, default=1)
    created_date = Column(DateTime, default=datetime.utcnow)
    client_id = Column(Integer, ForeignKey("client.id"))
    room_id = Column(Integer, ForeignKey("room.id"))

    client = relationship("Client", back_populates="reservation")
    room = relationship("Room", back_populates="reservation")