from fastapi import HTTPException
from database import db_connection


def leeftijf_controle(spelerleeftijd):
    if spelerleeftijd < 16:
        raise HTTPException(status_code=400, detail="Speler is te jong (jonger dan 16 jaar)")
    elif spelerleeftijd > 45:
        raise HTTPException(status_code=400, detail="Speler is te oud (ouder dan 45 jaar)")

def statestiek_controle(spelerstatistiek):
    if spelerstatistiek < 10:
        raise HTTPException(status_code=400, detail="Speler is te slecht (statestiek kleiner dan 10)")
    elif spelerstatistiek > 99:
        raise HTTPException(status_code=400, detail="Speler is te goed (statestiek groter dan 99)")

def team_id_controle(teamid):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM teams WHERE team_id = %s", (teamid,))
    team = cursor.fetchone()
    if team is None:
        cursor.close()
        raise HTTPException(status_code=404, detail="Team niet gevonden")
    cursor.close()

def speler_id_controle(speler_id):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM spelers WHERE speler_id = %s", (speler_id,))
    speler = cursor.fetchone()  # Haal de speler op
    if speler is None:  # Controleer of de speler niet bestaat
        cursor.close()
        raise HTTPException(status_code=404, detail="Speler niet gevonden")
    cursor.close()

def competitie_id_controle(competitie_id):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM competities WHERE competitie_id = %s", (competitie_id,))
    competitie = cursor.fetchone()
    if competitie is None:
        cursor.close()
        raise HTTPException(status_code=404, detail="Competitie niet gevonden")
    cursor.close()