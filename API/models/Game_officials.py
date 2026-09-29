from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Game_officials(Base):
    __tablename__ = "Game_officials"
    
    game_id : Mapped[str] = mapped_column(String(10), primary_key=True)
    officials_name : Mapped[str] = mapped_column(String(150), nullable=False)
    officials_type : Mapped[str] = mapped_column(String(20), nullable=False)