from pydantic import BaseModel, Field

class Game_penalties_Model(BaseModel):
    penaltySeverity : str = Field(max_length=25)
    penaltyMinutes : int = Field(ge=2, le=10)

class Game_penalties_Out(Game_penalties_Model):
    play_id : str = Field(max_length=15)