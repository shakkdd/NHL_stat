from pydantic import BaseModel, Field
from uuid import UUID

class Game_play_player(BaseModel):
    
    player_id : UUID
    game_id : UUID
    play_id : UUID
    player_type : str = Field(max_length=50)