from fastapi import APIRouter
from pydantic import BaseModel,ConfigDict

router = APIRouter()

competities = [
    {'id_competitie': 1, 'naam_competitie': 'Eredivisie', 'land_competitie': 'Nederland'},
    {'id_competitie': 2, 'naam_competitie': 'Premier league', 'land_competitie': 'Engeland'}
]

class competitieBase(BaseModel):
    id_competitie: int
    naam_competitie: str
    land_competitie: str

class CreateCompetitie(competitieBase):
    model_config = ConfigDict(from_attributes=True)

@router.get('/competitie')
async def get_competities() -> list[competitieBase]:
    return competities

@router.post('/competitie')
async def create_competities(competitie:CreateCompetitie) -> list[competitieBase]:
    competities.append(competitie)
    return competities

#Verwijdert een speler op basis van ID
@router.delete('/competitie/{id_competitie}')
async def delete_competitie(competitie_id: int) -> competitieBase:
    global competities
    for i in range(len(competities)):
        if competities[i]['id_competitie'] == competitie_id:
            deleted_competitie = competities.pop(i)
            return deleted_competitie
    return {"error": "competitie not found"}


