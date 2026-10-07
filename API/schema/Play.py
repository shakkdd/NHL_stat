from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class Play_model(BaseModel):
    
    game_id : UUID
    for_team_id : UUID | None
    against_team_id : UUID | None
    event : str = Field(max_length=50)
    secondary_type : str |None = Field(max_length=50)
    x : int | None
    y : int | None
    period : int
    period_type : str = Field(max_length=50)
    period_time : int
    period_time_remaining : int
    date_time : datetime
    goals_away : int = Field(ge=0)
    goals_home : int = Field(ge=0)
    description : str | None = Field(max_length=250)
    st_x : int | None
    st_y : int | None
    
class Play_out(Play_model):
    
    play_id : UUID