from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict
from typing import List
app = FastAPI()

spelers = [
    {'id_speler': 1, 'naam_speler':  'Laurens', 'leeftijd': 24, 'afkomst': 'Nederland', 'statistieken': 55, 'transferwaarde': 20,
     'naam_team': 'Ajax'},
]

class SpelerBase(BaseModel):
    id_speler: int
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

class CreateSpeler(SpelerBase):
    model_config = ConfigDict(from_attributes=True)

@app.get('/spelers/')
async def get_spelers() -> list[SpelerBase]:
    return spelers

@app.post('/spelers')
async def create_speler(speler:CreateSpeler) -> list[SpelerBase]:
    spelers.append(speler)
    return spelers

@app.delete('/spelers/{speler_id}')
async def delete_speler(id_speler: int) -> SpelerBase:
    global spelers
    for speler_id, in range(len(spelers)):
        speler = spelers[speler_id]
        if speler['id_speler'] == id_speler:
            deleted_speler = spelers.pop(speler_id)
            return deleted_speler
    return {"error": "Speler not found"}