from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid
from uuid import UUID
import uuid
from datetime import date

class Players(Base):
    __tablename__ = "Players"
    
    player_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, default= uuid.uuid4)
    first_name : Mapped[str] = mapped_column(String(50), nullable=False)
    last_name : Mapped[str] = mapped_column(String(50), nullable=False)
    nationality : Mapped[str] = mapped_column(String(3), nullable=False)
    birth_city : Mapped[str] = mapped_column(String(100), nullable=False)
    primary_position : Mapped[str] = mapped_column(String(2), nullable=False)
    birth_date : Mapped[date] = mapped_column(nullable=False)
    height : Mapped[str] = mapped_column(String(10), nullable=True)
    height_cm : Mapped[float] = mapped_column(nullable=True)
    weight : Mapped[float] = mapped_column(nullable=True)
    shootsCatches : Mapped[str] = mapped_column(String(1),nullable=True)
    