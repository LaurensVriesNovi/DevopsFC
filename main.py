from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict

App = FastAPI()


class SpelerBase(BaseModel):
    naam: str
    leeftijd: int
    statistieken: int
    transferwaarde: int
    team_naam: str



