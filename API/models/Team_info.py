from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Team_info(Base):
    __tablename__ = "Team_info"
    
    team_id : Mapped[int] = mapped_column(primary_key=True)
    franchise_id : Mapped[int] = mapped_column(nullable= False)
    shortName : Mapped[str] = mapped_column(String(50), nullable=False)
    teamName : Mapped[str] = mapped_column(String(50), nullable=False)
    abbreviation : Mapped[str] = mapped_column(String(3), nullable=False)