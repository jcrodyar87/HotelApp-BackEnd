from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, date

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
    updated_date: datetime = datetime.utcnow()

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
    updated_date: datetime = datetime.utcnow()

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

class RoomType(BaseModel):
    id: Optional[int]
    name: str
    status: int

    class Config:
        orm_mode=True

class RoomTypeUpdate(BaseModel):
    name: str
    status: int
    updated_date: datetime = datetime.utcnow()

    class Config:
        orm_mode=True

class Room(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float
    capacity: int
    room_type_id: Optional[int] | None = None
    status: int

    class Config:
        orm_mode=True

class RoomUpdate(BaseModel):
    name: str
    description: str
    price: float
    capacity: int
    room_type_id: Optional[int] | None = None
    status: int
    updated_date: datetime = datetime.utcnow()

    class Config:
        orm_mode=True

class RoomWithRoomType(Room):
    created_date: Optional[datetime]
    room_type: Optional[RoomType] = None

class Response(BaseModel):
    message: str

class Country(BaseModel):
    id: Optional[int]
    name: str
    alpha3: str
    status: int

    class Config:
        orm_mode=True

class CountryUpdate(BaseModel):
    name: str
    alpha3: str
    status: int
    updated_date: datetime = datetime.utcnow()

    class Config:
        orm_mode=True

class Client(BaseModel):
    id: Optional[int]
    firstname: str
    lastname: str
    document: str
    phone: str
    email: str
    reservations_quantity: Optional[int]
    last_reservation:  Optional[datetime] = datetime.utcnow()
    status: int
    country_id: Optional[int] | None = None

    class Config:
        orm_mode=True

class ClientFull(Client):
    created_date: Optional[datetime]

class ClientUpdate(BaseModel):
    firstname: str
    lastname: str
    document: str
    phone: str
    email: str
    reservations_quantity: Optional[int]
    last_reservation:  Optional[datetime]
    status: int
    updated_date: datetime = datetime.utcnow()
    country_id: Optional[int]

    class Config:
        orm_mode=True

class ClientWithCountry(Client):
    created_date: Optional[datetime]
    country: Optional[Country] = None

class Reservation(BaseModel):
    id: Optional[int]
    checkin: date
    checkout: date
    adults: int
    children: int
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
    adults: int
    children: int
    total: float
    done_payment: float
    pending_payment: float
    status: int
    updated_date: datetime = datetime.utcnow()
    client_id: Optional[int]
    room_id: Optional[int]
    
    class Config:
        orm_mode=True

class ReservationEmail(BaseModel):
    id: Optional[int]

class AccountingDocument(BaseModel):
    id: Optional[int]
    number: str
    client_number: str
    client_name: str
    client_address: str
    issue_date: date
    type: int
    currency_type: int
    total_sale: float
    tax: float
    total: float
    status: int | None = None
    reservation_id: Optional[int] | None = None

    class Config:
        orm_mode=True

class AccountingDocumentUpdate(BaseModel):
    number: str
    client_number: str
    client_name: str
    client_address: str
    issue_date: date
    type: int
    currency_type: int
    total_sale: float
    tax: float
    total: float
    status: int
    updated_date: datetime = datetime.utcnow()
    reservation_id: Optional[int]
    
    class Config:
        orm_mode=True

class ReservationWithClientAndRoom(Reservation):
    client: Optional[Client] = None
    room: Optional[Room] = None

class ReservationWithClientAndRoomAndAccountingDocument(Reservation):
    client: Optional[Client] = None
    room: Optional[Room] = None
    accounting_document: Optional[AccountingDocument] = None

class ClosedSchedule(BaseModel):
    id: Optional[int]
    start_date: date
    end_date: date
    description: str
    status: int | None = None
    room_id: Optional[int] | None = None

    class Config:
        orm_mode=True
    
class ClosedScheduleUpdate(BaseModel):
    start_date: date
    end_date: date
    description: str
    status: int
    updated_date: datetime = datetime.utcnow()
    room_id: Optional[int]
    
    class Config:
        orm_mode=True


class ClosedScheduleWithRoom(ClosedSchedule):
    room: Optional[Room] = None