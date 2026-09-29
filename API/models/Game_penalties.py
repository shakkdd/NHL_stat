from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Game_penalties(Base):
    __tablename__ = "Game_penalties"
    
    play_id : Mapped[str] = mapped_column(String(15), primary_key=True)
    penaltySeverity : Mapped[str] = mapped_column(String(25), nullable=False)
    penaltyMinutes : Mapped[int] = mapped_column(nullable=False)