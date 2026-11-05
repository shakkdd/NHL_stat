from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID

class Game_skater_stats_out(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    game_id : UUID
    team_id : UUID
    player_id : UUID
    time_on_ice : int = Field(ge=0)
    assists : int = Field(ge=0)
    goals : int = Field(ge=0)
    shots : int = Field(ge=0)
    power_play_goals : int = Field(ge=0)
    power_play_assists : int = Field(ge=0)
    penalty_minutes : int = Field(ge=0)
    face_off_wins : int = Field(ge=0)
    face_off_taken : int = Field(ge=0)
    short_handed_goals : int = Field(ge=0)
    short_handed_assists : int = Field(ge=0)
    plus_minus : int
    even_time_on_ice : int = Field(ge=0)
    short_handed_time_on_ice : int = Field(ge=0)
    power_play_time_on_ice : int = Field(ge=0)