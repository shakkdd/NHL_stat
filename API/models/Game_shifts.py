from database import Base
from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

class Game_shifts(Base):
    __tablename__ = "Game_shifts"
    
    shift_id : Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    game_id : Mapped[str] = mapped_column(String(10), nullable=False)
    player_id : Mapped[str] = mapped_column(String(7), nullable=False)
    period : Mapped[int] = mapped_column(nullable=False)
    shift_start : Mapped[int] = mapped_column(nullable=False)
    shift_end : Mapped[int] = mapped_column(nullable=False)