from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from API.database import init_db

@asynccontextmanager
async def lifespan(app : FastAPI):
    init_db()
    yield

app = FastAPI( title="NHL", lifespan=lifespan, description="API des match NHL de 2000 à 2020")

@app.get("/health", tags=["Supervision"])
def verifier_sante():
    return {"status" : "OK","service": "NHL-API"}