from fastapi import APIRouter, Depends, Response, status
from API.database import getdb
from API.schema.Team import Team_out, Team_model
from API.models.Team import Team
from sqlalchemy.orm import Session
from sqlalchemy import select

router = APIRouter(prefix="/Teams", tags=["Teams"])

@router.get("", response_model=list[Team_out])
def get_team(db : Session = Depends(getdb)):
    return db.scalars(select(Team).order_by(Team.team_name))

@router.post("", response_model=Team_out)
def create_team(team_in : Team_model, db : Session = Depends(getdb)):
    team_add = Team(**team_in.model_dump())
    db.add(team_add)
    db.commit()
    db.refresh(team_add)
    return team_add

@router.delete("", status_code= status.HTTP_204_NO_CONTENT)
def delete_team(team_id : str, db : Session = Depends(getdb)):
    team_del = db.get(Team, team_id)
    db.delete(team_del)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)