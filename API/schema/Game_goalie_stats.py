from pydantic import BaseModel, Field
from uuid import UUID

class Game_goalie_stats(BaseModel):
    
    team_id : UUID
    player_id = UUID
    game_id = UUID
    time_on_ice : int = Field(ge=0)
    assist : int = Field(ge=0)
    goals : int = Field(ge=0)
    PIM : int = Field(ge=0)
    shots : int = Field(ge=0)
    saves : int = Field(ge=0)
    power_play_save : int = Field(ge=0)
    short_handed_save : int = Field(ge=0)
    even_save : int = Field(ge=0)
    short_handed_shots_against : int = Field(ge=0)
    power_play_shots_against : int = Field(ge=0)
    even_shots_against : int = Field(ge=0)
    save_percentage : float = Field(ge=0)
    power_play_saves_percentage : float = Field(ge=0)
    even_strenght_save_percentage : int = Field(ge=0)