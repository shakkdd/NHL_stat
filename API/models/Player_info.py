from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

class Player_info(Base):
    __tablename__ = "Player_info"
    
    player_id : Mapped[str] = mapped_column(String(7), unique=True, nullable=False)
    firstName : Mapped[str] = mapped_column(String(100), nullable=False)
    lastName : Mapped[str] = mapped_column(String(100), nullable=False)
    nationality : Mapped[str] = mapped_column(String(3), nullable=False)
    birthCity : Mapped[str] = mapped_column(String(100), nullable=False)
    primaryPosition : Mapped[str] = mapped_column(String(2), nullable=False)
    birthDate : Mapped[date] = mapped_column(nullable=False)
    height : Mapped[str] = mapped_column(String(10), nullable=False)
    height_cm : Mapped[float] = mapped_column(nullable=False)
    weight : Mapped[int] = mapped_column(nullable=False)
    shootsCatches : Mapped[str] = mapped_column(String(1), nullable=False)
    