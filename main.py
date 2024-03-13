from fastapi import FastAPI
from app import teams, spelers, competities
from logging_config import setup_logging

# Configure logging
logger = setup_logging()
from typing import List
app = FastAPI()
app.include_router(teams.router)
app.include_router(spelers.router)
app.include_router(competities.router)


@app.get('/')
async def Home():
    tekst="Welkom op onze pagina"
    return tekst
