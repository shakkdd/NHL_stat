from pydantic import BaseModel, Field

class Game_officials_Model(BaseModel):
    officials_name : str = Field(max_length=150)
    officials_type : str = Field(max_length=20)
    
class Game_Officials_Out(Game_officials_Model):
    game_id : str = Field(max_length=20)