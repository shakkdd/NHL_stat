from pydantic import BaseModel, Field
from uuid import UUID

class Game_shift_model(BaseModel):
    
    game_id : UUID
    player_id : UUID
    period : int
    shift_start : int
    shift_end : int