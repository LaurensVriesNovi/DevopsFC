from fastapi import FastAPI
from competities import competities_router
from teams import teams_router
from spelers import spelers_router

from logger import logger
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware, BaseHTTPMiddleware
app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
logger.info('Starting API.')


app.include_router(spelers_router)
app.include_router(teams_router)
app.include_router(competities_router)
