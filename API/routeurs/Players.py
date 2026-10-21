from fastapi import APIRouter, Depends, Query
from datetime import date
from API.database import getdb
from sqlalchemy.orm import Session
from sqlalchemy import select
from API.models.Player import Players
from API.schema.Player import Player_out

router = APIRouter(prefix="/player", tags=["player"])

@router.get("", response_model=list[Player_out])
def get_player(db : Session = Depends(getdb),
    limit : int = Query(10, ge=1, le=50),
    page: int = Query(0, ge=0),
    first_name: str = Query(None),
    last_name: str = Query(None),
    nationality : str = Query(None),
    birth_city : str = Query(None),
    min_birth_date : date = Query(None, description="Format : AAAA-MM-DD"),
    max_birth_date : date = Query(None, description="Format : AAAA-MM-DD"),
    position: str = Query(None),
    min_heigth: int = Query(None),
    max_heigth: int = Query(None),
    min_weight: int = Query(None),
    max_weight: int = Query(None),
    shoots_catches: str = Query(None, description="L or R")):
    
    query = select(Players)
    
    #ajout des filtre
    if first_name:
        query = query.where(Players.first_name.islike(f"%{first_name}"))
        
    if last_name:
        query = query.where(Players.last_name.islike(f"%{last_name}"))
    
    if nationality:
        query = query.where(Players.nationality == nationality)
        
    if birth_city:
        query = query.where(Players.birth_city == birth_city)
        
    if min_birth_date:
        query = query.where(Players.birth_date >= min_birth_date)
        
    if max_birth_date:
        query = query.where(Players.birth_date <= max_birth_date)
        
    if position:
        query = query.where(Players.primary_position == position)
        
    if min_heigth:
        query = query.where(Players.height_cm >= min_heigth)
        
    if max_heigth:
        query = query.where(Players.height_cm <= max_weight)
    
    if min_weight:
        query = query.where(Players.weight >= min_weight)
        
    if max_weight:
        query = query.where(Players.weight <= max_weight)
        
    if shoots_catches:
        query.where(Players.shoots_catches == shoots_catches)
    
    query = query.offset(page).limit(limit)
    
    return db.scalars(query)