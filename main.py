from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict

App = FastAPI()


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



