from fastapi import APIRouter
from DevopsFC.database import fetch_tuples, db_connection

spelers_router = APIRouter()

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

@spelers_router.get('/spelers')
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

@spelers_router.post('/spelers')
async def create_speler(spelernaam: str, spelerland: str, spelerleeftijd: int, spelerstatistiek: int, teamid: int):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO spelers(naam, land, leeftijd, statistiek, team_id) VALUES (%s, %s, %s, %s, %s)",
                   (spelernaam, spelerland, spelerleeftijd, spelerstatistiek, teamid))
    cursor.close()
    return "speler toegevoegd"

@spelers_router.put("/spelers/{speler_id}")
async def update_speler(speler_id: int, spelerleeftijd: int, spelerstatistiek: int, teamid: int):
    cursor = db_connection.cursor()
    cursor.execute("UPDATE spelers SET leeftijd = %s, statistiek = %s, team_id = %s WHERE speler_id = %s",
                   (spelerleeftijd, spelerstatistiek, teamid, speler_id))
    cursor.close()
    return "speler gewijzigd"
    raise HTTPException(status_code=404, detail="speler niet gevonden")

@spelers_router.delete('/spelers/{speler_id}')
async def delete_speler(speler_id: int):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM spelers WHERE speler_id = %s", (speler_id,))
    cursor.close()
    return "speler verwijderd"
    raise HTTPException(status_code=404, detail="speler niet gevonden")
