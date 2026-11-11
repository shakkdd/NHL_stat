from fastapi import APIRouter, Depends, HTTPException, Query
from datetime import date, datetime, time, timedelta
from API.database import getdb
from sqlalchemy.orm import Session
from sqlalchemy import select
from API.models.Game import Game
from API.schema.Game import Game_out
from uuid import UUID

router = APIRouter(prefix="/Game", tags=["Game"])

@router.get("", response_model=list[Game_out])
def get_game(db : Session = Depends(getdb),
    limit : int = Query(10, ge=1, le=50),
    page : int = Query(0, ge=0),
    season : str = Query(None),
    type : str = Query(None),
    date : date = Query(None),
    team_1 : str = Query(None),
    team_2 : str = Query(None),
    outcome : str = Query(None),
    venu : str = Query(None)):
    
    query = select(Game)
    
    if season:
        query = query.where(Game.season == season)
    
    if type:
        query = query.where(Game.type == type)
        
    if date:
        start_of_day = datetime.combine(date, time.min)
        query = query.where(
            Game.date_time >= start_of_day,
            Game.date_time < start_of_day + timedelta(days=1),
        )
        
    if team_1:
        query = query.where((Game.away_team_id == team_1) | (Game.home_team_id == team_1))
    
    if team_2:
        query = query.where((Game.away_team_id == team_2) | (Game.home_team_id == team_2))
        
    if outcome:
        query = query.where(Game.outcome == outcome)
    
    if venu:
        query = query.where(Game.venue == venu)
        
    query = query.offset(page).limit(limit)
    
    return db.scalars(query)

@router.get("/result")
def get_outcome(db : Session = Depends(getdb)):
    return db.scalars(select(Game.outcome).distinct()).all()

@router.get("/place")
def get_place(db : Session = Depends(getdb)):
    return db.scalars(select(Game.venue).distinct()).all()

@router.get("/season")
def get_season(db : Session = Depends(getdb)):
    return db.scalars(select(Game.season).distinct()).all()

@router.get("/id")
def get_game_id(db : Session = Depends(getdb)):
    return db.scalars(select(Game.game_id).distinct()).all()

@router.get("/{game_id}", response_model=Game_out)
def get_game_by_id(game_id: UUID, db: Session = Depends(getdb)):
    game = db.get(Game, game_id)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return {
        "game_id": game.game_id,
        "season": game.season,
        "type": game.type,
        "date_time": game.date_time,
        "away_team_id": game.away_team_id,
        "home_team_id": game.home_team_id,
        "away_goals": game.away_goals,
        "home_goals": game.home_goals,
        "outcome": game.outcome,
        "venue": game.venue,
        "venue_time_zone": game.venue_time_zone,
        "venue_time_zone_offset": game.venue_time_zone_offset,
        "venue_time_zone_tz": game.venue_time_zone_tz,
    }