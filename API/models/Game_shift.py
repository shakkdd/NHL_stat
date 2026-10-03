from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid, ForeignKeyConstraint
from uuid import UUID

class Game_Shift(Base):
    __tablename__ = "Game_Shifts"
    
    player_id : Mapped[UUID] = mapped_column(Uuid,primary_key=True ,nullable=False)
    game_id : Mapped[UUID] = mapped_column(Uuid,primary_key=True ,nullable=False)
    period: Mapped[int] = mapped_column(nullable=False)
    shift_start: Mapped[int] = mapped_column(nullable=False)
    shift_end: Mapped[int] = mapped_column(nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(["player_id"], ["Players.player_id"], name="fk_game_shifts_player"),
        ForeignKeyConstraint(["game_id"], ["Games.game_id"], name="fk_game_shifts_game"),
    )