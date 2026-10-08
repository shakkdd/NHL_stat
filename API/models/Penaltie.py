from API.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid, ForeignKeyConstraint
from uuid import UUID
import uuid

class Penalitie(Base):
    __tablename__ = "Penalities"
    
    play_id : Mapped[UUID] =mapped_column(primary_key=True, nullable=False)
    penality_severity : Mapped[str] = mapped_column(String(25), nullable=False)
    penalitie_minutes : Mapped[int] = mapped_column(nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(["play_id"], ["Plays.play_id"], name="fk_penalties_play_id"),
    )