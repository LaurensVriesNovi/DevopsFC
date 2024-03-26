from database import db_connection
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict

app = FastAPI()



class competitiebase(BaseModel):
    naam_competitie: str
    land_competitie: str


class CreateCompetitie(competitiebase):
    model_config = ConfigDict(from_attributes=True)


class SpelerAanpassen(BaseModel):
    leeftijd: int
    statistieken: int
    team_id: int


# Verbindingsgegevens voor de PostgreSQL-database
db_connection.autocommit = True

def fetch_tuples(query):
    cursor = db_connection.cursor()
    cursor.execute(query)
    tuples = cursor.fetchall()
    cursor.close()
    return tuples


def get_competitie_tuples():
    return fetch_tuples("SELECT * FROM competities")


def get_team_tuples():
    return fetch_tuples("SELECT * FROM teams")


def get_speler_tuples():
    return fetch_tuples("SELECT * FROM spelers")


def waarde_berekenen(speler):
    leeftijd_speler = speler[3]
    if leeftijd_speler < 22:
        waarde_leeftijd = 50 + 8 * (leeftijd_speler - 16)
    elif leeftijd_speler > 22:
        waarde_leeftijd = 100 - (leeftijd_speler - 22) * 4
    else:
        waarde_leeftijd = 100
    totale_transferwaarde = int(waarde_leeftijd * (1 / 2 * speler[4]) * 10000)
    return totale_transferwaarde


# COMPETITIES COMPETITIES COMPETITIES
# COMPETITIES COMPETITIES COMPETITIES
# COMPETITIES COMPETITIES COMPETITIES
@app.get("/competities")
def get_competitieswaardes():
    # Stap 1: Ophalen van gegevens
    competities = get_competitie_tuples()
    teams = get_team_tuples()
    spelers = get_speler_tuples()

    # Lijst om de informatie van elke competitie bij te houden
    competitie_info = []

    # Stap 2: Bereken de waarde van elke competitie
    for competitie in competities:
        competitie_id = competitie[0]
        competitie_naam = competitie[1]
        competitie_land = competitie[2]
        competitie_waarde = 0
        competitie_spelers = 0

        # Stap 3: Loop over teams en spelers om de totale waarde van de competitie te berekenen
        for team in teams:
            for speler in spelers:
                if speler[5] == team[0] and team[2] == competitie_id:
                    totale_transferwaarde = waarde_berekenen(speler)
                    competitie_waarde += totale_transferwaarde
                    competitie_spelers += 1

        # Voeg de informatie van de competitie toe aan de lijst
        competitie_info.append({
            'id': competitie_id,
            "naam": competitie_naam,
            "land": competitie_land,
            "waarde": competitie_waarde,
            "aantal spelers": competitie_spelers
        })

    # Return de lijst met de informatie van alle competities
    return competitie_info

@app.post('/competities')
async def create_competities(competitienaam: str, competitieland: str):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO competities(naam, land) VALUES (%s, %s)", (competitienaam, competitieland))
    cursor.close()
    return "competitie toegevoegd"


# SPELERS SPELERS SPELERS
# SPELERS SPELERS SPELERS
# SPELERS SPELERS SPELERS
@app.get('/spelers')
async def get_spelers():
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT s.speler_id AS speler_id, s.naam AS speler_naam, s.land AS speler_land, s.leeftijd AS speler_leeftijd, s.statistiek AS speler_statistiek, t.naam AS team_naam FROM spelers s INNER JOIN teams t ON s.team_id = t.team_id")
    spelers = cursor.fetchall()
    cursor.close()
    speler_info = []
    for speler in spelers:
        transferwaarde = waarde_berekenen(speler)
        opgemaakte_transferwaarde = '{0:,.0f}'.format(transferwaarde).replace(',',
                                                                              '.')  # Opmaak met duizendtallen gescheiden door punten
        speler_info.append({
            "id": speler[0],
            "naam": speler[1],
            "land": speler[2],
            "leeftijd": speler[3],
            "statistiek": speler[4],
            "team_naam": speler[5],
            "waarde": opgemaakte_transferwaarde
        })

    return speler_info


@app.post('/spelers')
async def create_speler(spelernaam: str, spelerland: str, spelerleeftijd: int, spelerstatistiek: int, teamid: int):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO spelers(naam, land, leeftijd, statistiek, team_id) VALUES (%s, %s, %s, %s, %s)",
                   (spelernaam, spelerland, spelerleeftijd, spelerstatistiek, teamid))
    cursor.close()
    return "speler toegevoegd"


# Verwijdert een speler op basis van ID
@app.delete('/spelers/{speler_id}')
async def delete_speler(speler_id: int):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM spelers WHERE speler_id = %s", (speler_id,))
    cursor.close()
    return "speler verwijderd"
    raise HTTPException(status_code=404, detail="speler niet gevonden")


@app.put("/spelers/{speler_id}")
async def update_speler(speler_id: int, spelerleeftijd: int, spelerstatistiek: int, teamid: int):
    cursor = db_connection.cursor()
    cursor.execute("UPDATE spelers SET leeftijd = %s, statistiek = %s, team_id = %s WHERE speler_id = %s",
                   (spelerleeftijd, spelerstatistiek, teamid, speler_id))
    cursor.close()
    return "speler gewijzigd"
    raise HTTPException(status_code=404, detail="speler niet gevonden")

# TEAM TEAM TEAM
# TEAM TEAM TEAM
# TEAM TEAM TEAM

@app.get("/teams")
async def get_teams():
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT t.team_id, t.naam, c.naam AS Competitie FROM Teams t INNER JOIN competities c ON t.competitie_id = c.competitie_id")
    teams = cursor.fetchall()
    cursor.close()
    return teams

@app.post('/teams')
async def create_team(teamnaam: str, competitie_id: int):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO teams(naam, competitie_id) VALUES (%s, %s)", (teamnaam, competitie_id))
    cursor.close()
    return "team toegevoegd"
