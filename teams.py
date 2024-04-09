from fastapi import APIRouter, HTTPException
from database import fetch_tuples, db_connection

teams_router = APIRouter()

def get_team_tuples():
    return fetch_tuples("SELECT * FROM teams")

@teams_router.get("/teams")
async def get_teams():
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT t.team_id, t.naam, c.naam AS Competitie FROM Teams t INNER JOIN competities c ON t.competitie_id = c.competitie_id")
    teams = cursor.fetchall()
    cursor.close()
    return teams

@teams_router.post('/teams')
async def create_team(teamnaam: str, competitie_id: int):
    cursor = db_connection.cursor()
    
    # Controleer of de competitie bestaat
    cursor.execute("SELECT * FROM competities WHERE id = %s", (competitie_id,))
    competitie = cursor.fetchone()
    if competitie is None:
        cursor.close()
        raise HTTPException(status_code=404, detail="Competitie niet gevonden")

    # Voeg het team toe als de competitie bestaat
    cursor.execute("INSERT INTO teams(naam, competitie_id) VALUES (%s, %s)", (teamnaam, competitie_id))
    cursor.close()
    return "Team toegevoegd"
