from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Game(Base):
    __tablename__ = "Game"
    
    game_id : Mapped[str] = mapped_column(String(10), unique=True)
    season : Mapped[str] = mapped_column(String(8), nullable=False)
    date_time_GMT : Mapped[datetime] = mapped_column(nullable=False)
    away_team_id : Mapped[int] = mapped_column(nullable=False)
    home_team_id : Mapped[int] = mapped_column(nullable=False)
    away_goals : Mapped[int] = mapped_column(nullable=False)
    home_goals : Mapped[int] = mapped_column(nullable=False)
    outcome : Mapped[str] = mapped_column(String(50), nullable=False)
    home_rink_side_start : Mapped[str] = mapped_column(String(5), nullable=False)
    venue : Mapped[str] = mapped_column(String(100), nullable=False)
    venue_time_zone_id : Mapped[str] = mapped_column(String(100), nullable=False)
    venue_time_zone_tz : Mapped[str] = mapped_column(String(3), nullable=False)