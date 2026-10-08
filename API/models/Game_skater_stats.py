from API.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid, ForeignKeyConstraint
from uuid import UUID

class Game_Skater_stats(Base):
    __tablename__ = "Game_skater_stats"
    
    game_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    player_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    team_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, nullable=False)
    time_on_ice : Mapped[int] = mapped_column(nullable=False)
    assists : Mapped[int] = mapped_column(nullable=False)
    goals : Mapped[int] = mapped_column(nullable=False)
    shots : Mapped[int] = mapped_column(nullable=False)
    hits : Mapped[int] = mapped_column(nullable=False)
    power_play_goals : Mapped[int] = mapped_column(nullable=False)
    power_play_assists : Mapped[int] = mapped_column(nullable=False)
    penalty_minutes : Mapped[int] = mapped_column(nullable=False)
    face_of_wins : Mapped[int] = mapped_column(nullable=False)
    face_of_taken : Mapped[int] = mapped_column(nullable=False)
    takeaways : Mapped[int] = mapped_column(nullable=False)
    giveaways : Mapped[int] = mapped_column(nullable=False)
    short_handed_goals : Mapped[int] = mapped_column(nullable=False)
    short_handed_assists : Mapped[int] = mapped_column(nullable=False)
    blocked : Mapped[int] = mapped_column(nullable=False)
    plus_minus : Mapped[int] = mapped_column(nullable=False)
    even_time_on_ice : Mapped[int] = mapped_column(nullable=False)
    short_handed_time_on_ice : Mapped[int] = mapped_column(nullable=False)
    power_play_time_on_ice : Mapped[int] = mapped_column(nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(["team_id"], ["Teams.team_id"], name="fk_game_skater_stats_team_id"),
        ForeignKeyConstraint(["player_id"], ["Players.player_id"], name = "fk_game_skater_stats_player_id"),
        ForeignKeyConstraint(["game_id"], ["Games.game_id"], name="fk_game_skater_stats_game_id")
    )