from fastapi import APIRouter, Depends, HTTPException, Query
from datetime import date, datetime, time, timedelta
from API.database import getdb
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select
from API.models.Game import Game
from API.models.Team import Team
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
    
    away_team = aliased(Team)
    home_team = aliased(Team)
    query = (
        select(
            Game,
            away_team.abbreviation.label("away_team_abbreviation"),
            home_team.abbreviation.label("home_team_abbreviation"),
        )
        .outerjoin(away_team, Game.away_team_id == away_team.team_id)
        .outerjoin(home_team, Game.home_team_id == home_team.team_id)
    )
    
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
        query = query.where(
            (away_team.abbreviation == team_1) | (home_team.abbreviation == team_1)
        )
    
    if team_2:
        query = query.where(
            (away_team.abbreviation == team_2) | (home_team.abbreviation == team_2)
        )
        
    if outcome:
        query = query.where(Game.outcome == outcome)
    
    if venu:
        query = query.where(Game.venue == venu)
        
    query = query.offset(page).limit(limit)
    
    rows = db.execute(query).all()
    return [
        {
            **Game_out.model_validate(game, from_attributes=True).model_dump(),
            "away_team_abbreviation": away_abbreviation,
            "home_team_abbreviation": home_abbreviation,
        }
        for game, away_abbreviation, home_abbreviation in rows
    ]

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
    away_team = aliased(Team)
    home_team = aliased(Team)
    query = (
        select(
            Game,
            away_team.abbreviation.label("away_team_abbreviation"),
            home_team.abbreviation.label("home_team_abbreviation"),
        )
        .outerjoin(away_team, Game.away_team_id == away_team.team_id)
        .outerjoin(home_team, Game.home_team_id == home_team.team_id)
        .where(Game.game_id == game_id)
    )
    row = db.execute(query).one_or_none()
    if row is None:
        raise HTTPException(status_code=404, detail="Game not found")
    game, away_abbreviation, home_abbreviation = row
    return {
        **Game_out.model_validate(game, from_attributes=True).model_dump(),
        "away_team_abbreviation": away_abbreviation,
        "home_team_abbreviation": home_abbreviation,
    }