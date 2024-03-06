from fastapi import FastAPI
from app import teams, spelers, competities
from typing import List
app = FastAPI()
app.include_router(teams.router)
app.include_router(spelers.router)
app.include_router(competities.router)

#@app.put("/superheroes/{id}", response_model=Superhero)
#async def update_superhero(id: int, superhero: Superhero):
#    for i, hero in enumerate(superheroes_data):
#        if hero["id"] == id:
#            superheroes_data[i] = superhero.dict()
#            superheroes_data[i]['id'] = id
#            return Superhero(**superheroes_data[i])
#    raise HTTPException(status_code=404, detail="Superhero not found")

@app.get('/')
async def Home():
    tekst="Welkom op onze pagina"
    return tekst