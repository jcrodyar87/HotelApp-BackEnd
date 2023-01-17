from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/clients",tags=["clients"],responses={404:{"message":"No encontrado"}})

class Client(BaseModel):
    id: int
    firstname: str
    lastname: str
    document: str
    phone: str
    email: str
    status: int

clients_list = [Client(id=1, firstname="Juan", lastname="Rodriguez", document="44854480", phone="966744497", email="jcry87@gmail.com", status=1),
                Client(id=2, firstname="Carlos", lastname="Yarmas", document="44854481", phone="966744498", email="jcry1987@gmail.com", status=1)]


@router.get("/")
async def clients():
    return clients_list

@router.get("/{id}")
async def client(id: int):
    return search_client(id)

def search_client(id: int):
    room = filter(lambda room: room.id == id, clients_list)
    try:
        return list(room)[0]
    except:
        raise HTTPException(status_code=404, detail="No se ha encontrado el cliente")