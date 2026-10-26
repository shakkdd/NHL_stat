from fastapi import APIRouter, Depends, HTTPException, Response, status
from API.database import getdb
from API.schema.Team import Team_out, Team_model
from API.models.Team import Team
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from uuid import UUID

router = APIRouter(prefix="/Teams", tags=["Teams"])

@router.get("", response_model=list[Team_out])
def get_team(db : Session = Depends(getdb)):
    return db.scalars(select(Team).order_by(Team.team_name))

@router.post("", response_model=Team_out)
def create_team(team_in : Team_model, db : Session = Depends(getdb)):
    team_add = Team(**team_in.model_dump())
    db.add(team_add)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A team with this abbreviation already exists",
        ) from exc
    db.refresh(team_add)
    return team_add

@router.delete("", status_code= status.HTTP_204_NO_CONTENT)
def delete_team(team_id : str, db : Session = Depends(getdb)):
    team_del = db.get(Team, team_id)
    db.delete(team_del)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("", response_model=Team_out)
def update_team(team_id : UUID, team_in : Team_model, db : Session = Depends(getdb)):
    team_update = db.get(Team, team_id)
    if team_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")

    for field, value in team_in.model_dump().items():
        setattr(team_update, field, value)

    db.commit()
    db.refresh(team_update)
    return team_update