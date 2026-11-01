from fastapi import APIRouter, Depends, Path, Query
from API.database import getdb
from sqlalchemy.orm import Session
from sqlalchemy import select
from API.models.Play import Play
from uuid import UUID

router = APIRouter(prefix="/Game_info", tags=["Game_info"])

@router.get("/{game_id}")
def get_game_info(game_id: str, db: Session = Depends(getdb), limit: int = Query(10, ge=1, le=50), page: int = Query(0, ge=0)):
    
    query = select(Play).where(Play.game_id == game_id)
    
    if game_id:
        query = query.where(Play.game_id == game_id)

    query = query.offset(page).limit(limit).order_by(Play.date_time)
        
    return db.scalars(query).all()