from pydantic import BaseModel, Field
from uuid import UUID

class Game_team_stats_model(BaseModel):
    
    game_id : UUID
    team_id : UUID
    HoA : str  = Field(max_length=4)
    won : bool
    setteld_in : str = Field(max_length=4)
    head_coach : str = Field(max_length=100)
    goals : int = Field(ge=0)
    shots : int = Field(ge=0)
    hits : int = Field(ge=0)
    pim : int = Field(ge=0)
    power_play_opportunities : int = Field(ge=0)
    power_play_goals : int = Field(ge=0)
    face_off_win_percentage : float