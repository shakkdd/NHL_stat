from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="NHL", 
    description="API des match NHL de 2000 à 2020")