from database import Base
from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

class Game_scratches(Base):
    __tablename__ = "Game_scratches"
    
    game_scratches_id : Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    game_id : Mapped[str] = mapped_column(String(10), nullable=False)
    team_id : Mapped[int] = mapped_column(nullable=False)
    player_id : Mapped[str] = mapped_column(nullable=False)