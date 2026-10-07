from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid, ForeignKeyConstraint
from uuid import UUID
import uuid
from datetime import datetime

class Game(Base):
    __tablename__ = "Games"
    
    game_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    season : Mapped[str] = mapped_column(String(8), nullable=False)
    type : Mapped[str] = mapped_column(String(1),nullable=False)
    date_time = Mapped[datetime] = mapped_column(nullable=False)
    away_taem_id = Mapped[UUID] = mapped_column(Uuid, nullable=False)
    hom_team_id = Mapped[UUID] = mapped_column(Uuid, nullable=False)
    away_goals : Mapped[int] = mapped_column(nullable=False)
    home_goals : Mapped[int] = mapped_column(nullable=False)
    outcome = Mapped[str] = mapped_column(String(50), nullable=False)
    venue : Mapped[str] = mapped_column(String(100), nullable=False)
    venue_time_zone : Mapped[str] = mapped_column(String(100), nullable=False)
    venue_time_zone_offset : Mapped[int] = mapped_column(nullable=False)
    venue_time_zone_tz : Mapped[str] = mapped_column(String(3), nullable=False)
    
    __table_args__ =(
        ForeignKeyConstraint(["away_team_id"], ["Teams.team_id"], name="fk_game_away_team"),
        ForeignKeyConstraint(["home_team_id"], ["Teams.team_id"], name="fk_game_home_team")
    )