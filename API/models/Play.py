from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid, ForeignKeyConstraint
from uuid import UUID
from datetime import datetime
import uuid

class Play(Base):
    __tablename__ = "Plays"
    
    play_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, default= uuid.uuid4)
    for_team_id : Mapped[UUID] = mapped_column(nullable=True)
    against_team_id : Mapped[UUID] = mapped_column(nullable=True)
    event : Mapped[str] = mapped_column(String(50), nullable=False)
    secondary_type : Mapped[str] = mapped_column(String(50), nullable=True)
    x : Mapped[int] = mapped_column(nullable=True)
    y : Mapped[int] = mapped_column(nullable=True)
    period : Mapped[int] = mapped_column(nullable=False)
    period_type : Mapped[str] = mapped_column(String(50),nullable=False)
    period_time : Mapped[int] = mapped_column(nullable=False)
    period_time_remaining : Mapped[int] = mapped_column(nullable=False)
    date_time : Mapped[datetime] = mapped_column(nullable=False)
    goals_away : Mapped[int] = mapped_column(nullable=False)
    goals_home : Mapped[int] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column(String(250), nullable=True)
    st_x : Mapped[int] = mapped_column(nullable=True)
    st_y : Mapped[int] = mapped_column(nullable=True)
    
    
    __table_args__ = (
        ForeignKeyConstraint(["for_team_id"], ["Teams.team_id"], name="fk_plays_for_team_id"),
        ForeignKeyConstraint(["against_team_id"],["Teams.team_id"], name="fk_plays_against_team_id")
    )