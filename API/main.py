import os
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from API.database import init_db
from API.routeurs import Teams, Players, Game, game_play, goalie_details, player_details

@asynccontextmanager
async def lifespan(app : FastAPI):
    init_db()
    yield

app = FastAPI( title="NHL", lifespan=lifespan, description="API des match NHL de 2000 à 2020")

frontend_origins = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost:8501,http://127.0.0.1:8501",
    ).split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=frontend_origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Supervision"])
def verifier_sante():
    return {"status" : "OK","service": "NHL-API"}

app.include_router(Teams.router)
app.include_router(Players.router)
app.include_router(player_details.router)
app.include_router(goalie_details.router)
app.include_router(Game.router)
app.include_router(game_play.router)