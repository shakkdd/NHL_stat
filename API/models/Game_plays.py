from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Game_plays(Base):
    __tablename__ = "Game_plays"
    
    play_id : Mapped[str] = mapped_column(String(15), primary_key=True, nullable=False)
    game_id : Mapped[str] = mapped_column(String(10), nullable=False)
    team_id_for : Mapped[int] = mapped_column(nullable=True)
    team_id_against : Mapped[int] = mapped_column(nullable=True)
    event : Mapped[str] = mapped_column(String(100), nullable=False)
    secondaryType : Mapped[str] = mapped_column(String(100), nullable=True)
    x : Mapped[int] = mapped_column(nullable=True)
    y : Mapped[int] = mapped_column(nullable=True)
    period : Mapped[int] = mapped_column(nullable=False)
    periodType : Mapped[str] = mapped_column(String(10),nullable=False)
    periodTime : Mapped[int] = mapped_column(nullable=False)
    periodTimeRemaining : Mapped[int] = mapped_column(nullable=False)
    dateTime :Mapped[datetime] = mapped_column(nullable=False)
    goals_away : Mapped[int] = mapped_column(nullable=False)
    goals_home : Mapped[int] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column(String(255), nullable= True)
    st_x : Mapped[int] = mapped_column(nullable=True)
    st_y : Mapped[int] = mapped_column(nullable=True)