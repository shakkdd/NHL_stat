from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid, ForeignKeyConstraint
from uuid import UUID

class Game_Teams_Stats(Base):
    __tablename__ = "Game_team_stats"
    
    game_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    team_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    HoA : Mapped[str] = mapped_column(String(4), nullable=False)
    won : Mapped[bool] = mapped_column(nullable=False)
    setteld_in : Mapped[str] = mapped_column(String(3), nullable=False)
    head_coach : Mapped[str] = mapped_column(String(100), nullable=False)
    goals : Mapped[int] = mapped_column(nullable=False)
    shots : Mapped[int] = mapped_column(nullable=False)
    pim : Mapped[int] = mapped_column(nullable=False)
    power_play_opportunities : Mapped[int] = mapped_column(nullable=False)
    power_play_goals : Mapped[int] = mapped_column(nullable=False)
    face_off_win_percentage : Mapped[float] = mapped_column(nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(["team_id"], ["Teams.team_id"], name="fk_game_team_stats_team_id"),
        ForeignKeyConstraint(["game_id"], ["Games.game_id"], name="fk_game_team_stats_game_id")
    )