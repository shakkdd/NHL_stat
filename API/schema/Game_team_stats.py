from pydantic import BaseModel, Field
from uuid import UUID

class Game_team_stats_model(BaseModel):
    
    team_id : UUID
    game_id : UUID
    HoA : str  = Field(max_length=4)
    won : bool
    setteld_in : str = Field(max_length=4)
    head_coach : str = Field(max_length=100)
    goals : int = Field(ge=0)
    shots : int = Field(ge=0)
    hits : int = Field(ge=0)
    PIM : int = Field(ge=0)
    power_play_opportunities : int = Field(ge=0)
    power_play_goals : int = Field(ge=0)
    face_off_win_percentage : float
    giveaways : int = Field(ge=0)
    takeaways : int = Field(ge=0)
    blocked : int = Field(ge=0)
    start_rink_side : str = Field(max_length=5)