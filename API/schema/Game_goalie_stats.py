from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class Game_goalie_stats_out(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_id: UUID
    player_id: UUID
    team_id: UUID
    team_abbreviation: str | None = None
    time_on_ice: int = Field(ge=0)
    assists: int = Field(ge=0)
    goals: int = Field(ge=0)
    pim: int = Field(ge=0)
    shots: int = Field(ge=0)
    saves: int = Field(ge=0)
    power_play_saves: int = Field(ge=0)
    short_handed_saves: int = Field(ge=0)
    even_save: int = Field(ge=0)
    short_handed_shots_against: int = Field(ge=0)
    even_shots_against: int = Field(ge=0)
    power_play_shots_against: int = Field(ge=0)
    decision: str | None = Field(max_length=1)
    save_percentage: float = Field(ge=0)
    power_play_saves_percentage: float = Field(ge=0)
    even_strenght_save_percentage: float = Field(ge=0)


class Goalie_global_stats(BaseModel):
    total_games: int
    total_time_on_ice: int
    total_assists: int
    total_goals: int
    total_pim: int
    total_shots: int
    total_saves: int
    total_power_play_saves: int
    total_short_handed_saves: int
    total_even_saves: int
    total_power_play_shots_against: int
    total_short_handed_shots_against: int
    total_even_shots_against: int
    total_wins: int
    total_losses: int
    total_save_percentage: float | None
    total_power_play_save_percentage: float | None
    total_short_handed_save_percentage: float | None
    total_even_strength_save_percentage: float | None
