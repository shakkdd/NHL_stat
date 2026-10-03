from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class Game_model(BaseModel):
    season : str = Field(max_length=8)
    type : str = Field(max_length=1)
    date_time : datetime
    away_team_id : UUID
    home_team_id : UUID
    outcome : str = Field(max_length=50)
    away_goals : int = Field(max_digits=2, ge=0)
    home_goals : int = Field(max_digits=2, ge=0)
    home_rink_side_strat : str = Field(max_length=5)
    venue : str = Field(max_length=100)
    venue_time_zone : str = Field(max_length=100)
    venue_time_zone_offset : int
    venue_time_zone_tz : str = Field(max_length=3, min_length=3)
    
class Game_out(Game_model):
    game_id : UUID