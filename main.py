from fastapi import FastAPI
from competities import competities_router
from teams import teams_router
from spelers import spelers_router


app = FastAPI()
app.include_router(spelers_router)
app.include_router(teams_router)
app.include_router(competities_router)
