from fastapi import FastAPI
from routes import clients, rooms
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(clients.router)
app.include_router(rooms.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return {"Hello": "World"}

