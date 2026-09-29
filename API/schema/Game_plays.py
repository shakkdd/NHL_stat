from pydantic import BaseModel, Field
from datetime import datetime

class Game_plays_Model(BaseModel):
    game_id : str = Field(max_length=10)
    team_id_for : int | None
    team_id_agaisnt : int | None
    event : str = Field(max_length=250)
    secondaryType : str | None = Field(max_length=250)
    x : int | None
    y : int | None
    period : int = Field(ge=1, le=4)
    periodType : str = Field(max_length=10)
    periodTime : int = Field(ge=0)
    periodTimeRemaining : int = Field(ge=0)
    dateTime : datetime
    goals_away : int = Field(ge=0)
    goals_home : int = Field(ge=0)
    description : str | None = Field(max_length=255)
    st_x : int | None
    st_y : int | None
    
class Game_plays_Out(Game_plays_Model):
    play_id : int