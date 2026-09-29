from pydantic import BaseModel, Field

class Game_shift_Model(BaseModel):
    game_id : str = Field(max_length=10)
    player_id : str = Field(max_length=7)
    period : int = Field(ge=1, le=4)
    shift_start : int = Field(ge=0)
    shift_end : int = Field(ge=0)
    
class Game_shift_Out(Game_shift_Model):
    shift_id : int
    