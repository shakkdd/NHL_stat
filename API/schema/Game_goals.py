from pydantic import BaseModel, Field
from uuid import UUID

class Game_goalModel(BaseModel):
    play_id : UUID
    game_winning_goals : bool
    empty_net : bool
    
class Game_goalOut(Game_goalModel):
    goals_id : UUID