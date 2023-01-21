from fastapi import FastAPI
from routes import roles, users, auth, clients, rooms, reservations
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(roles.router)
app.include_router(users.router)
app.include_router(clients.router)
app.include_router(rooms.router)
app.include_router(reservations.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


