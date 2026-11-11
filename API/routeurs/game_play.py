from fastapi import APIRouter, Depends
from API.database import getdb
from sqlalchemy.orm import Session
from sqlalchemy import select
from API.models.Play import Play

router = APIRouter(prefix="/Game_info", tags=["Game_info"])

@router.get("/{game_id}")
def get_game_info(game_id: str, db: Session = Depends(getdb)):
    
    query = select(Play).where(Play.game_id == game_id)

    query = query.order_by(Play.date_time)
        
    return db.scalars(query).all()