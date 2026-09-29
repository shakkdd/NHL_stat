from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Game_skater_stats(Base):
    __tablename__ = "Game_skater_stats"
    
    game_id : Mapped[str] = mapped_column(String(10), primary_key=True, nullable=False)
    player_id : Mapped[str] = mapped_column(String(7), primary_key=True, nullable=False)
    team_id : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    timeOnIce : Mapped[int] = mapped_column(nullable= False)
    assists : Mapped[int] = mapped_column(nullable=False)
    goals : Mapped[int] = mapped_column(nullable=False)
    shots : Mapped[int] = mapped_column(nullable=False)
    hits : Mapped[int] = mapped_column(nullable=False)
    powerPlayGoals : Mapped[int] = mapped_column(nullable=False)
    powerPlayAssists : Mapped[int] = mapped_column(nullable=False)
    penaltyMinutes : Mapped[int] = mapped_column(nullable=False)
    faceOffWins : Mapped[int] = mapped_column(nullable=False)
    faceoffTaken : Mapped[int] = mapped_column(nullable=False)
    takeaways : Mapped[int] = mapped_column(nullable=False)
    giveaways : Mapped[int] = mapped_column(nullable=False)
    shortHandedGoals : Mapped[int] = mapped_column(nullable=False)
    shortHandedAssists : Mapped[int] = mapped_column(nullable=False)
    blocked : Mapped[int] = mapped_column(nullable=False)
    plusMinus : Mapped[int] = mapped_column(nullable=False)
    evenTimeOnIce : Mapped[int] = mapped_column(nullable=False)
    shortHandedTimeOnIce : Mapped[int] = mapped_column(nullable=False)
    powerPlayTimeOnIce : Mapped[int] = mapped_column(nullable=False)