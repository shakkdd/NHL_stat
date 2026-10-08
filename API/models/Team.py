from API.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid
from uuid import UUID
import uuid

class Team(Base):
    __tablename__ = "Teams"
    
    team_id : Mapped[UUID] = mapped_column(Uuid, primary_key=True, default= uuid.uuid4)
    short_name : Mapped[str] = mapped_column(String(50), nullable=False)
    team_name : Mapped[str] = mapped_column(String(50), nullable=False)
    abbreviation : Mapped[str] = mapped_column(String(3), nullable=False, unique=True)
    