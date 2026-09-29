from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Game_goalie_stats(Base):
    __tablename__ = "Game_goalie_stats"
    
    game_id : Mapped[str] = mapped_column(String(15), primary_key=True, nullable=False)
    player_id : Mapped[str] = mapped_column(String(7), primary_key=True, nullable=False)
    team_id : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    timeOnIce : Mapped[int] = mapped_column(nullable=False)
    assists : Mapped[int] = mapped_column(nullable=False)
    goals : Mapped[int] = mapped_column(nullable=False)
    pim : Mapped[int] = mapped_column(nullable=False)
    shots : Mapped[int] = mapped_column(nullable=False)
    saves : Mapped[int] = mapped_column(nullable=False)
    powerPlaySaves : Mapped[int] = mapped_column(nullable=False)
    shortHandedSaves : Mapped[int] = mapped_column(nullable=False)
    evenSaves : Mapped[int] = mapped_column(nullable=False)
    shortHandedShotsAgainst: Mapped[int] = mapped_column(nullable=False)
    evenShotsAgainst : Mapped[int] = mapped_column(nullable=False)
    powerPlayShotsAgainst : Mapped[int] = mapped_column(nullable=False)
    decision : Mapped[str] = mapped_column(String(1), nullable=True)
    savePercentage : Mapped[float] = mapped_column(nullable=False)
    powerPlaySavePercentage : Mapped[float] = mapped_column(nullable=False)
    evenStrengthSavePercentage : Mapped[float] = mapped_column(nullable=False)
