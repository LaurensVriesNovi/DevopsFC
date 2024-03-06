from fastapi import FastAPI
from app import teams, spelers, competities
from typing import List
app = FastAPI()
app.include_router(teams.router)
app.include_router(spelers.router)
app.include_router(competities.router)