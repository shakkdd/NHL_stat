from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date

class Player_model(BaseModel):
    
    first_name : str = Field(max_length=50)
    last_name : str = Field(max_length=50)
    nationality : str = Field(min_length=3, max_length=3)
    birth_city : str = Field(max_length=100)
    primary_position : str = Field(max_length=2)
    birth_date : date
    
class Player_out(Player_model):
    player_id : UUID