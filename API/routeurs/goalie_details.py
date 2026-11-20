from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy import case, func, select
from sqlalchemy.orm import Session

from API.database import getdb
from API.models.Game_goalie_stats import Game_goalie_stats
from API.models.Team import Team
from API.schema.Game_goalie_stats import Game_goalie_stats_out, Goalie_global_stats

router = APIRouter(prefix="/Goalie_stat", tags=["Goalie_stat"])


@router.get("/{player_id}", response_model=list[Game_goalie_stats_out])
def get_goalie_match_stats(
    player_id: UUID,
    team_id: UUID | None = Query(None),
    limit: int = Query(10, ge=1, le=50),
    page: int = Query(0, ge=0),
    db: Session = Depends(getdb),
):
    query = (
        select(Game_goalie_stats, Team.abbreviation.label("team_abbreviation"))
        .join(Team, Game_goalie_stats.team_id == Team.team_id)
        .where(Game_goalie_stats.player_id == player_id)
    )
    if team_id:
        query = query.where(Game_goalie_stats.team_id == team_id)

    query = query.order_by(Game_goalie_stats.game_id).offset(page).limit(limit)
    rows = db.execute(query).all()
    return [
        {
            **Game_goalie_stats_out.model_validate(stats).model_dump(),
            "team_abbreviation": team_abbreviation,
        }
        for stats, team_abbreviation in rows
    ]


@router.get("/{player_id}/global_stat", response_model=Goalie_global_stats | None)
def get_goalie_global_stats(
    player_id: UUID,
    team_id: UUID | None = Query(None),
    db: Session = Depends(getdb),
):
    query = select(
        func.count(func.distinct(Game_goalie_stats.game_id)).label("total_games"),
        func.sum(Game_goalie_stats.time_on_ice).label("total_time_on_ice"),
        func.sum(Game_goalie_stats.assists).label("total_assists"),
        func.sum(Game_goalie_stats.goals).label("total_goals"),
        func.sum(Game_goalie_stats.pim).label("total_pim"),
        func.sum(Game_goalie_stats.shots).label("total_shots"),
        func.sum(Game_goalie_stats.saves).label("total_saves"),
        func.sum(Game_goalie_stats.power_play_saves).label("total_power_play_saves"),
        func.sum(Game_goalie_stats.short_handed_saves).label("total_short_handed_saves"),
        func.sum(Game_goalie_stats.even_save).label("total_even_saves"),
        func.sum(Game_goalie_stats.power_play_shots_against).label("total_power_play_shots_against"),
        func.sum(Game_goalie_stats.short_handed_shots_against).label("total_short_handed_shots_against"),
        func.sum(Game_goalie_stats.even_shots_against).label("total_even_shots_against"),
        func.sum(case((Game_goalie_stats.decision == "W", 1), else_=0)).label("total_wins"),
        func.sum(case((Game_goalie_stats.decision == "L", 1), else_=0)).label("total_losses"),
    ).where(Game_goalie_stats.player_id == player_id)

    if team_id:
        query = query.where(Game_goalie_stats.team_id == team_id)

    totals = db.execute(query).mappings().one()
    if not totals["total_games"]:
        return None

    result = dict(totals)

    def percentage(saves: int, shots_against: int) -> float | None:
        return round(saves * 100 / shots_against, 1) if shots_against else None

    result["total_save_percentage"] = percentage(result["total_saves"], result["total_shots"])
    result["total_power_play_save_percentage"] = percentage(
        result["total_power_play_saves"],
        result["total_power_play_shots_against"],
    )
    result["total_short_handed_save_percentage"] = percentage(
        result["total_short_handed_saves"],
        result["total_short_handed_shots_against"],
    )
    result["total_even_strength_save_percentage"] = percentage(
        result["total_even_saves"],
        result["total_even_shots_against"],
    )
    return result


@router.get("/{player_id}/Teams")
def get_goalie_teams(player_id: UUID, db: Session = Depends(getdb)):
    query = (
        select(Team.team_id, Team.abbreviation)
        .select_from(Game_goalie_stats)
        .join(Team, Game_goalie_stats.team_id == Team.team_id)
        .where(Game_goalie_stats.player_id == player_id)
        .distinct()
        .order_by(Team.abbreviation)
    )
    return [
        {"team_id": team_id, "abbreviation": abbreviation}
        for team_id, abbreviation in db.execute(query).all()
    ]
