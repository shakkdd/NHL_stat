from pydantic import BaseModel, Field
from uuid import UUID

class Team_model(BaseModel):
    short_name : str = Field(max_length=50)
    team_name : str = Field(max_length=50)
    abbreviation : str = Field(min_length=3, max_length=3)
    
class Team_out(Team_model):
    team_id : UUID