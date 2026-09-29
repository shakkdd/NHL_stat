from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Game_goals(Base):
    __tablename__ = "Game_goals"
    
    play_id : Mapped[str] = mapped_column(String(15), primary_key=True, nullable=False)
    strength : Mapped[str] = mapped_column(String(20), nullable=False)
    game_winning_goal : Mapped[bool] = mapped_column(nullable=False, default=False)
    empty_net : Mapped[bool] = mapped_column(nullable= False, default=False)
    