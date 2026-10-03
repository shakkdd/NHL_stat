from pydantic import BaseModel, Field
from uuid import UUID

class Game_skater_stats(BaseModel):

    team_id : UUID
    player_id : UUID
    game_id : UUID
    time_on_ice : int = Field(ge=0)
    assists : int = Field(ge=0)
    goals : int = Field(ge=0)
    shots : int = Field(ge=0)
    hits : int = Field(ge=0)
    power_play_goals : int = Field(ge=0)
    power_play_assists : int = Field(ge=0)
    penalty_minutes : int = Field(ge=0)
    face_of_wins : int = Field(ge=0)
    face_of_taken : int = Field(ge=0)
    takeaways : int = Field(ge=0)
    giveaways : int = Field(ge=0)
    short_handed_goals : int = Field(ge=0)
    short_handed_assists : int = Field(ge=0)
    blocked : int = Field(ge=0)
    plus_minus : int
    even_time_on_ice : int = Field(ge=0)
    short_handed_time_on_ice : int = Field(ge=0)
    power_play_time_on_ice : int = Field(ge=0)