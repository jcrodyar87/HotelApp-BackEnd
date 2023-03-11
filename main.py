from fastapi import FastAPI
from routes import roles, users, auth, countries, clients, room_types, rooms, reservations, accounting_documents, closed_schedules, modules
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
	allow_headers=["*"],
    max_age=3600,
)

app.include_router(auth.router)
app.include_router(roles.router)
app.include_router(users.router)
app.include_router(countries.router)
app.include_router(clients.router)
app.include_router(room_types.router)
app.include_router(rooms.router)
app.include_router(reservations.router)
app.include_router(accounting_documents.router)
app.include_router(closed_schedules.router)
app.include_router(modules.router)

@app.get('/')
def redirect_doc():
    return RedirectResponse(url=f"/docs/", status_code=303)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/admin-angular")
async def read_index():
    return FileResponse('/../HotelAppAdmin/index.html')
