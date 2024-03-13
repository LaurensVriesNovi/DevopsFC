from fastapi import FastAPI
from app import teams, spelers, competities
from typing import List
app = FastAPI()
app.include_router(teams.router)
app.include_router(spelers.router)
app.include_router(competities.router)


@app.get('/')
async def Home():
    tekst="Welkom op onze pagina"
    return tekst


for speler in spelers:
    leeftijd_speler = speler['leeftijd']
    if leeftijd_speler < 22:
        waarde_leeftijd = 50 + 8 * (leeftijd_speler - 16)
    elif leeftijd_speler > 22:
        waarde_leeftijd = 100 - (leeftijd_speler - 22) * 4
    else:
        waarde_leeftijd = 100
    totale_transferwaarde = int(waarde_leeftijd * (1/2 * speler['statistieken']) * 10000)
    speler.update({'transferwaarde':totale_transferwaarde})
    print(f'De totale transferwaarde van {speler['naam_speler']} is {totale_transferwaarde}')
print(spelers)
gezochte_competitie = 'Premier League'
competitie_waarde = 0

for team in teams:
    if team['competitie'] == gezochte_competitie:
        for speler in spelers:
            if speler['naam_team'] == team['naam_team']:
                competitie_waarde += speler['transferwaarde']
print(competitie_waarde)