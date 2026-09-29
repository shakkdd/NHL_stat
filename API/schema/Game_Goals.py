from pydantic import BaseModel, Field

class Game_goals_Model(BaseModel):
    strenght : str = Field(max_length=20)
    game_winning_goal : bool = Field(default=False)
    empty_net : bool = Field(default=False)

class Game_goals_Out(Game_goals_Model):
    play_id : str