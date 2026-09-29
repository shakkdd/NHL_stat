from pydantic import BaseModel, Field

class Team_info_Model(BaseModel):
    franchise_id : int
    shortName : str = Field(max_length=3, min_length=3)
    teamName : str = Field(min_length=3)
    abbreviation : str = Field(max_length=3)
    
class Team_info_Out(Team_info_Model):
    team_id : int