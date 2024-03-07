from fastapi import APIRouter
from pydantic import BaseModel,ConfigDict

# lets crash this guy

router = APIRouter()

spelers = [
    {'id_speler': 1, 'naam_speler':  'Laurens', 'leeftijd': 24, 'afkomst': 'Nederland', 'statistieken': 55,
     'transferwaarde': 20, 'naam_team': 'Ajax'},

    {'id_speler': 2, 'naam_speler': 'Lean', 'leeftijd': 20, 'afkomst': 'Nederland', 'statistieken': 80,
     'transferwaarde': 20, 'naam_team': 'Liverpool'},

    {'id_speler': 3, 'naam_speler': 'Sam', 'leeftijd': 20, 'afkomst': 'Nederland', 'statistieken': 99,
     'transferwaarde': 21, 'naam_team': 'Az'},
]




class SpelerBase(BaseModel):
    id_speler: int
    naam_speler: str
    leeftijd: int
    afkomst: str
    statistieken: int
    transferwaarde: int
    naam_team: str

class output(BaseModel):
    uitleg: str
    output_tekst: SpelerBase

class CreateSpeler(SpelerBase):
    model_config = ConfigDict(from_attributes=True)

@router.get('/spelers/')
async def get_spelers() -> list[SpelerBase]:
    return spelers


@router.get('/spelers/{id_speler}')
async def get_spelers_id(id_speler: int) -> output:
    tekst= "dit is de uitleg voor deze pagina"
    gevraagd = spelers[id_speler - 1]
    return output(uitleg = tekst , output_tekst= gevraagd)

@router.put("/spelers/{id_speler}")
async def update_speler(id_speler: int, speler: SpelerBase):
    for i, speler_data in enumerate(spelers):
        if speler_data["id_speler"] == id_speler:
            if speler.naam_speler:
                speler_data["naam_speler"] = speler.naam_speler
            if speler.leeftijd:
                speler_data["leeftijd"] = speler.leeftijd
            return spelers[i]



#Maakt een nieuwe speler aan
@router.post('/spelers')
async def create_speler(speler:CreateSpeler) -> list[SpelerBase]:
    spelers.append(speler)
    return spelers

#Verwijdert een speler op basis van ID
@router.delete('/spelers/{speler_id}')
async def delete_speler(id_speler: int) -> SpelerBase:
    global spelers
    for speler_id in range(len(spelers)):
        speler = spelers[speler_id]
        if speler['id_speler'] == id_speler:
            deleted_speler = spelers.pop(speler_id)
            return deleted_speler
    return {"error": "Speler not found"}