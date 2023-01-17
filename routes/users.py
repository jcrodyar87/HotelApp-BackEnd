from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",tags=["users"],responses={404:{"message":"No encontrado"}})

class User(BaseModel):
    id: int
    username: str
    status: int

class UserDB(User):
    password: str

users_list = [User(id=1, username="admin@hotelapp.com", status=1),
         User(id=2, username="recepcionist@ghotelapp.com", status=1)]

@router.get("/")
async def users():
    return users_list

@router.get("/{id}")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")

@router.post("/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:   
        users_list.append(user)
        return user

@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="No se ha actualizado el usuario")
    else:
        return user

@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="No se ha eiminado el usuario")
