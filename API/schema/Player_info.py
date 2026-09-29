from pydantic import BaseModel, Field
from datetime import date

class Player_info_Model(BaseModel):
    firstName : str
    lastName : str
    nationality : str = Field(max_length=3)
    birthCity : str
    primaryPosition : str = Field(max_length=2)
    birthDate : date
    height : str
    height_cm : int = Field(max_digits=3)
    weight : int = Field(max_digits=3)
    shootsCatches : str = Field(max_length=1)
    
class Player_info_Out(Player_info_Model):
    player_id : int
    