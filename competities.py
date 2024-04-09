from fastapi import APIRouter
from spelers import get_speler_tuples, waarde_berekenen
from database import fetch_tuples, db_connection
from teams import get_team_tuples

competities_router = APIRouter()

def get_competitie_tuples():
    return fetch_tuples("SELECT * FROM competities")

@competities_router.get("/competities")
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
                    transferwaarde = waarde_berekenen(speler)
                    competitie_waarde += transferwaarde
                    competitie_spelers += 1

        # Opgemaakte transferwaarde na de loops
        opgemaakte_transferwaarde = '{0:,.0f}'.format(competitie_waarde).replace(',', '.')

        # Voeg de informatie van de competitie toe aan de lijst
        competitie_info.append({
            'id': competitie_id,
            "naam": competitie_naam,
            "land": competitie_land,
            "waarde": opgemaakte_transferwaarde,  # Opgemaakte transferwaarde
            "aantal spelers": competitie_spelers
        })

    # Return de lijst met de informatie van alle competities
    return competitie_info


@competities_router.post('/competities')
async def create_competities(competitie_naam: str, competitie_land: str):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO competities(naam, land) VALUES (%s, %s)", (competitie_naam, competitie_land))
    cursor.close()
    return "competitie toegevoegd"
