from fastapi import APIRouter, Depends, Query
from API.database import getdb
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from uuid import UUID
from API.models.Game_skater_stats import Game_Skater_stats
from API.models.Team import Team
from API.schema.Game_skater_stats import Game_skater_stats_out

router= APIRouter(prefix="/Player_stat", tags=["Player_stat"])


# fais une liste de tous les matchs d'un joueur avec ses stats, on peut filtrer par game_id et team_id, on peut aussi faire une pagination avec limit et page
@router.get("/{player_id}", response_model=list[Game_skater_stats_out])
def get_player_match_stat(player_id: UUID,
    team_id : UUID = Query(None),                 
    limit: int = Query(10, ge=1, le=50), 
    page: int = Query(0, ge=0), 
    db : Session = Depends(getdb)):
    
    query = (
        select(Game_Skater_stats, Team.abbreviation.label("team_abbreviation"))
        .join(Team, Game_Skater_stats.team_id == Team.team_id)
        .where(Game_Skater_stats.player_id == player_id)
    )
    
    if team_id:
       query = query.where(Game_Skater_stats.team_id == team_id)
    
    query = query.limit(limit).offset(page).order_by(Game_Skater_stats.game_id)
    
    rows = db.execute(query).all()
    return [
        {
            **Game_skater_stats_out.model_validate(stats).model_dump(),
            "team_abbreviation": team_abbreviation,
        }
        for stats, team_abbreviation in rows
    ]

@router.get("/{player_id}/global_stat")
def get_player_global_stat(player_id: UUID,
    team_id : UUID = Query(None),
    limit: int = Query(10, ge=1, le=50), 
    page: int = Query(0, ge=0), 
    db : Session = Depends(getdb)):
    
    query = (select
        (
            func.sum(Game_Skater_stats.time_on_ice).label("total_time_on_ice"),
            func.sum(Game_Skater_stats.assists).label("total_assists"),
            func.sum(Game_Skater_stats.goals).label("total_goals"),
            func.sum(Game_Skater_stats.shots).label("total_shots"),
            func.sum(Game_Skater_stats.power_play_goals).label("total_power_play_goals"),
            func.sum(Game_Skater_stats.power_play_assists).label("total_power_play_assists"),
            func.sum(Game_Skater_stats.power_play_time_on_ice).label("total_power_play_time_on_ice"),
            func.sum(Game_Skater_stats.face_off_taken).label("total_face_off_taken"),
            func.sum(Game_Skater_stats.face_off_wins).label("total_face_off_wins"),
            func.sum(Game_Skater_stats.short_handed_goals).label("total_short_handed_goals"),
            func.sum(Game_Skater_stats.short_handed_assists).label("total_short_handed_assists"),
            func.sum(Game_Skater_stats.short_handed_time_on_ice).label("total_short_handed_time_on_ice"),
            func.sum(Game_Skater_stats.plus_minus).label("total_plus_minus"),
            func.sum(Game_Skater_stats.penalty_minutes).label("total_penalty_minutes"),
            func.sum(Game_Skater_stats.even_time_on_ice).label("total_even_time_on_ice")
        )
        .group_by(Game_Skater_stats.player_id)
        .where(Game_Skater_stats.player_id == player_id)   
        )
    
    if team_id:
        query = query.where(Game_Skater_stats.team_id == team_id)
        
    query = query.limit(limit).offset(page)
    
    return db.execute(query).mappings().first()

@router.get("/{player_id}/Teams")
def get_player_teams(player_id: UUID, db: Session = Depends(getdb)):
    
    query = (
        select(Team.team_id, Team.abbreviation)
        .select_from(Game_Skater_stats)
        .join(Team, Game_Skater_stats.team_id == Team.team_id)
        .where(Game_Skater_stats.player_id == player_id)
        .distinct()
        .order_by(Team.abbreviation)
    )
    
    return [
        {"team_id": team_id, "abbreviation": abbreviation}
        for team_id, abbreviation in db.execute(query).all()
    ]