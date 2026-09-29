from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Game_plays_players(Base):
    __tablename__ = "Game_plays_players"
    
    play_id : Mapped[str] = mapped_column(String(15),primary_key=True, nullable=False)
    game_id : Mapped[str] = mapped_column(String(10), nullable=False)
    player_id : Mapped[str] = mapped_column(String(7), nullable=False)
    playerType : Mapped[str] = mapped_column(String(50), nullable=False)