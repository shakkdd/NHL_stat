from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class game_teams_stats(Base):
    __tablename__ = "game_teams_stats"
    
    game_id : Mapped[str] = mapped_column(String(10), primary_key=True, nullable=False)
    team_id : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    HoA : Mapped[str] = mapped_column(String(5), nullable=False)
    won : Mapped[bool] = mapped_column(nullable=False)
    settled_in : Mapped[str] = mapped_column(String(3), nullable=False)
    head_coach : Mapped[str] = mapped_column(String(100), nullable=False)
    goals : Mapped[int] = mapped_column(nullable=False)
    shot : Mapped[int] = mapped_column(nullable=False)
    hits : Mapped[int] = mapped_column(nullable=False)
    pim : Mapped[int]= mapped_column(nullable=False)
    powerPlayOpportunities : Mapped[int] = mapped_column(nullable=False)
    powerPlayGoals : Mapped[int] = mapped_column(nullable=False)
    faceOffWinPercentage : Mapped[float] = mapped_column(nullable=False)
    giveaways : Mapped[int] = mapped_column(nullable=False)
    takeaways : Mapped[int] = mapped_column(nullable=False)
    blocked : Mapped[int] = mapped_column(nullable=False)
    startRinkSide : Mapped[str] = mapped_column(String(5), nullable=False)
    