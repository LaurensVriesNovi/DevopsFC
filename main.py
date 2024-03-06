from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict
from typing import List
app = FastAPI()

#De data van de spelers
spelers = [
    {'id_speler': 1, 'naam_speler':  'Laurens', 'leeftijd': 24, 'afkomst': 'Nederland', 'statistieken': 55,
     'transferwaarde': 20, 'naam_team': 'Ajax'},

    {'id_speler': 2, 'naam_speler': 'Lean', 'leeftijd': 20, 'afkomst': 'Nederland', 'statistieken': 80,
     'transferwaarde': 20, 'naam_team': 'Liverpool'},

    {'id_speler': 3, 'naam_speler': 'Sam', 'leeftijd': 20, 'afkomst': 'Nederland', 'statistieken': 99,
     'transferwaarde': 21, 'naam_team': 'Az'},
]


teams = [
    {'naam_team': 'Ajax', 'competitie': 'Eredivisie', 'totale_transferwaarde': 200},
    {'naam_team': 'Liverpool', 'competitie': 'Premier League', 'totale_transferwaarde': 400},
    {'naam_team': 'Az', 'competitie': 'Eredivisie', 'totale_transferwaarde': 800}
]
#Het basemodel van de spelers, waar vast staat welke waarden een speler heeft.
class SpelerBase(BaseModel):
    id_speler: int
    naam_speler: str
    leeftijd: int
    afkomst: str
    statistieken: int
    transferwaarde: int
    naam_team: str

#Het basemodel van de competities, waar vast staat welke waarden een speler heeft.
class TeamBase(BaseModel):
    naam_team: str
    competitie: str
    totale_transferwaarde: int

#Het basemodel van de competities, waar vast staat welke waarden een speler heeft.
class competitieBase(BaseModel):
    naam_competitie: str
    land_competitie: str

class CreateSpeler(SpelerBase):
    model_config = ConfigDict(from_attributes=True)

#Haalt alle data van de spelers op
@app.get('/spelers/')
async def get_spelers() -> list[SpelerBase]:
    return spelers

#Maakt een nieuwe speler aan
@app.post('/spelers')
async def create_speler(speler:CreateSpeler) -> list[SpelerBase]:
    spelers.append(speler)
    return spelers

#Verwijdert een speler op basis van ID
@app.delete('/spelers/{speler_id}')
async def delete_speler(id_speler: int) -> SpelerBase:
    global spelers
    for speler_id in range(len(spelers)):
        speler = spelers[speler_id]
        if speler['id_speler'] == id_speler:
            deleted_speler = spelers.pop(speler_id)
            return deleted_speler
    return {"error": "Speler not found"}

@app.get('/teams')
async def get_teams() -> list[TeamBase]:
    return teams