from pydantic import BaseModel, Field
from datetime import datetime

class Game_Model(BaseModel):
    season : str = Field(max_length=8)
    date_time_GMT : datetime
    away_team_id : int
    home_team_id : int
    away_goals : int
    home_goals : int
    outcome : str = Field(max_length=50)
    home_rink_side_start : str = Field(max_length=5)
    venue : str = Field(max_length=100)
    venue_time_zone_id : str = Field(max_length=100)
    venue_time_zone_tz : str = Field(max_length=3)
    
class Game_Out(Game_Model):
    game_id : str