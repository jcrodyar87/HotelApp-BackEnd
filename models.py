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