from database import db_connection
from fastapi import FastAPI
from app.competities import competities_router
from app.teams import teams_router
from app.spelers import spelers_router
import socket

app = FastAPI()
app.include_router(competities_router)
app.include_router(teams_router)
app.include_router(spelers_router)

db_connection.autocommit = True

@app.get("/")
def read_root():
    return {"message": "Hello, World!", "pod": socket.gethostname()}




