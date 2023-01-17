from typing import Optional
from pydantic import BaseModel

class Room(BaseModel):
    id: Optional[int]
    name: str
    description: str
    type: str
    price: float
    capacity: int
    status: int

    class Config:
        orm_mode=True

class RoomUpdate(BaseModel):
    name: str
    description: str
    type: str
    price: float
    capacity: int
    status: int

    class Config:
        orm_mode=True

class Response(BaseModel):
    message: str

class Client(BaseModel):
    id: Optional[int]
    firstname: str
    lastname: str
    document: str
    phone: str
    email: str
    status: int

    class Config:
        orm_mode=True

class ClientUpdate(BaseModel):
    firstname: str
    lastname: str
    document: str
    phone: str
    email: str
    status: int

    class Config:
        orm_mode=True

class User(BaseModel):
    id: Optional[int]
    username: str
    status: int

    class Config:
        orm_mode=True

class UserUpdate(BaseModel):
    username: str
    status: int

    class Config:
        orm_mode=True