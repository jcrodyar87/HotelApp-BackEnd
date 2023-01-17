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