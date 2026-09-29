from pydantic import BaseModel, Field

class Game_plays_player_Model(BaseModel):
    game_id : str = Field(max_length=10)
    player_id : str = Field(max_length=7)
    playerType : str = Field(max_length=50)
    
class Game_plays_player_Out(Game_plays_player_Model):
    play_id : str = Field(max_length=15)