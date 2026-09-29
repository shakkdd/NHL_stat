from pydantic import BaseModel, Field

class Game_scratches_Model(BaseModel):
    game_id : str = Field(max_length=10)
    team_id : int
    player_id : str = Field(max_length=7)
    
class Game_scratches_Out(Game_scratches_Model):
    game_scratches_id : int