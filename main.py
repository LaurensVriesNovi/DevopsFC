from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict
from typing import List
app = FastAPI()

spelers = [
    {'naam_speler':  'Laurens', 'leeftijd': 24, 'afkomst': 'Nederland', 'statistieken': 55, 'transferwaarde': 20,
     'naam_team': 'Ajax'},
]

class SpelerBase(BaseModel):
    naam_speler: str
    leeftijd: int
    afkomst: str
    statistieken: int
    transferwaarde: int
    naam_team: str

class TeamBase(BaseModel):
    naam_team: str
    competitie: str
    totale_transferwaarde: int

class competitieBase(BaseModel):
    naam_competitie: str
    land_competitie: str


@app.get('/spelers/')
async def get_spelers() -> list[SpelerBase]:
    return spelers