from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, date

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

class Role(BaseModel):
    id: Optional[int]
    name: str
    modules: str
    status: int

    class Config:
        orm_mode=True

class RoleUpdate(BaseModel):
    name: str
    modules: str
    status: int

    class Config:
        orm_mode=True

class User(BaseModel):
    id: Optional[int]
    username: str
    firstname: str | None = None
    lastname: str | None = None
    password: str | None = None
    role_id: Optional[int] | None = None
    status: int | None = None

    class Config:
        orm_mode=True

class UserUpdate(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    status: int

    class Config:
        orm_mode=True

class UserAuth(BaseModel):
    username: str

class UserNewPassword(BaseModel):
    username: str
    password: str
    token: str

class UserWithRole(User):
    role: Optional[Role] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class Reservation(BaseModel):
    id: Optional[int]
    checkin: date
    checkout: date
    total: float
    done_payment: float
    pending_payment: float
    status: int | None = None
    client_id: Optional[int] | None = None
    room_id: Optional[int] | None = None

    class Config:
        orm_mode=True

class ReservationUpdate(BaseModel):
    checkin: date
    checkout: date
    total: float
    done_payment: float
    pending_payment: float
    status: int | None = None
    client_id: Optional[int] | None = None
    room_id: Optional[int] | None = None

    class Config:
        orm_mode=True

class ReservationWithClientAndRoom(Reservation):
    client: Optional[Client] = None
    room: Optional[Room] = None