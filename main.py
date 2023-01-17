from fastapi import FastAPI
from routes import roles, users, auth, clients, rooms
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(roles.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(clients.router)
app.include_router(rooms.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


