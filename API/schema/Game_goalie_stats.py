from pydantic import BaseModel, Field

class Game_goalie_stats_Model(BaseModel):
    player_id : str = Field(max_length=15)
    team_id : int
    timeOnIce : int = Field(ge=0)
    assists : int = Field(ge=0)
    goals : int = Field(ge=0)
    pim : int = Field(ge=0)
    shots : int = Field(ge=0)
    saves : int = Field(ge=0)
    powerPlaySaves : int = Field(ge=0)
    shortHandedSaves : int = Field(ge=0)
    evenSaves : int = Field(ge=0)
    shortHandedShotsAgainst : int = Field(ge=0)
    evenShotsAgainst : int = Field(ge=0)
    powerPlayShotsAgainst : int = Field(ge=0)
    decision : str | None = Field(max_length=1)
    savePercentage : float = Field(ge=0,le=1)
    powerPlaySavePercentage : float = Field(ge=0, le=1)
    evenStrengthSavePercentage : float = Field(ge=0, le=1)