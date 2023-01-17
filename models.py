from sqlalchemy import Column, Integer, String, Numeric, Text
from config.database import Base

class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    description = Column(Text())
    type = Column(String(150))
    price = Column(Numeric())
    capacity = Column(Integer)
    status = Column(Integer)

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    document = Column(String(100))
    phone = Column(String(100))
    email = Column(String(150))
    status = Column(Integer)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200))
    firstname = Column(String(250))
    lastname = Column(String(250))
    password = Column(String(250))
    status = Column(Integer)

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    modules = Column(Text())
    status = Column(Integer)
