from API.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid, ForeignKeyConstraint, String
from uuid import UUID

class Game_goalie_stats(Base):
    __tablename__ = "Game_goalie_stats"
    
    game_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    player_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    team_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    time_on_ice : Mapped[int] = mapped_column(nullable=False)
    assists : Mapped[int] = mapped_column(nullable=False)
    goals : Mapped[int] = mapped_column(nullable=False)
    pim : Mapped[int] = mapped_column(nullable=False)
    shots : Mapped[int] = mapped_column(nullable=False)
    saves : Mapped[int] = mapped_column(nullable=False)
    power_play_saves : Mapped[int] = mapped_column(nullable=False)
    short_handed_saves : Mapped[int] = mapped_column(nullable=False)
    even_save : Mapped[int] = mapped_column(nullable=False)
    short_handed_shots_against : Mapped[int] = mapped_column(nullable=False)
    power_play_shots_against : Mapped[int] = mapped_column(nullable=False)
    even_shots_against : Mapped[int] = mapped_column(nullable=False)
    decision : Mapped[str] = mapped_column(String(1),nullable=False)
    save_percentage : Mapped[float] = mapped_column(nullable=False)
    power_play_saves_percentage : Mapped[float] = mapped_column(nullable=False)
    even_strenght_save_percentage : Mapped[float] = mapped_column(nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(["team_id"], ["Teams.team_id"], name="fk_game_goalie_stats_team_id"),
        ForeignKeyConstraint(["player_id"], ["Players.player_id"], name="fk_game_goalie_stats_player_id"),
        ForeignKeyConstraint(["game_id"], ["Games.game_id"], name="fk_game_goalie_stats_game_id")
    )