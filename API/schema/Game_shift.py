from pydantic import BaseModel, Field
from uuid import UUID

class Game_shift_model(BaseModel):
    
    player_id : UUID
    game_id : UUID
    period : int
    shift_start : int
    shift_end : int