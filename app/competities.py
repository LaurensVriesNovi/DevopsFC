from fastapi import APIRouter
from pydantic import BaseModel,ConfigDict

router = APIRouter()

competities = [
    {'naam_competitie': 'Eredivisie', 'land_competitie': 'Nederland'},
    {'naam_competitie': 'Premier league', 'land_competitie': 'Engeland'}
]

class competitieBase(BaseModel):
    naam_competitie: str
    land_competitie: str