from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid, ForeignKeyConstraint
from uuid import UUID

class Game_play_player(Base):
    __tablename__ = "Game_play_players"
    
    player_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    game_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    play_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    player_type : Mapped[str] = mapped_column(String(50), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(["player_id"], ["Players.player_id"], name="fk_game_play_player_player_id"),
        ForeignKeyConstraint(["game_id"], ["Games.game_id"], name="fk_game_play_player_game_id"),
        ForeignKeyConstraint(["play_id"], ["Plays.play_id"], name="fk_game_play_player_play_id")
    )