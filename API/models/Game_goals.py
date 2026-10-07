from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid, ForeignKeyConstraint
from uuid import UUID

class Game_goals(Base):
    
    __tablename__ = "goals"
    
    goals_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    play_id : Mapped[UUID] = mapped_column(Uuid)
    strenght : Mapped[str] = mapped_column(String(50))
    game_winning_goals : Mapped[bool] = mapped_column(bool, default=False)
    empty_net : Mapped[bool] = mapped_column(bool, default=True)
    
    __table_args__ = (
        ForeignKeyConstraint(["play_id"], ["Plays.play_id"], name="fk_goals_play_id")
    )
    