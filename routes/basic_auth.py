from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    id: int
    username: str
    status: int

class UserDB(User):
    password: str

users_db = {
    "jcry87":{
        "username":"admin@hotelapp.com",
        "password":"12345",
        "status":1
    },
    "jcry1987":{
        "username":"recepcionist@ghotelapp.com",
        "password":"12345",
        "status":1
    }
}
#[UserDB(id=1, username="admin@hotelapp.com", password="12345", status=1),
#         UserDB(id=2, username="recepcionist@ghotelapp.com", password="12345", status=1)]

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate":"Bearer"})

    if user.status == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo")

    return user

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
