from fastapi import APIRouter
from pydantic import BaseModel,ConfigDict

router = APIRouter()

teams = [
    {'id_team': 1, 'naam_team': 'Ajax', 'competitie': 'Eredivisie', 'totale_transferwaarde': 200},
    {'id_team': 2, 'naam_team': 'Liverpool', 'competitie': 'Premier League', 'totale_transferwaarde': 400},
    {'id_team': 3, 'naam_team': 'Az', 'competitie': 'Eredivisie', 'totale_transferwaarde': 800}
]

class TeamBase(BaseModel):
    id_team: int
    naam_team: str
    competitie: str
    totale_transferwaarde: int

class CreateTeam(TeamBase):
    model_config = ConfigDict(from_attributes=True)

@router.get('/teams')
async def get_teams() -> list[TeamBase]:
    return teams

@router.post('/teams')
async def create_speler(team:CreateTeam) -> list[TeamBase]:
    teams.append(team)
    return teams

#Verwijdert een speler op basis van ID
@router.delete('/teams/{id_team}')
async def delete_team(team_id: int) -> TeamBase:
    global teams
    for i in range(len(teams)):
        if teams[i]['id_team'] == team_id:
            deleted_team = teams.pop(i)
            return deleted_team
    return {"error": "Speler not found"}