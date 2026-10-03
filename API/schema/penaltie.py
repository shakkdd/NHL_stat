from pydantic import BaseModel, Field
from uuid import UUID

class penalties_model(BaseModel):
    
    play_id : UUID
    penality_severity : str = Field(max_length=25)
    penalitie_minutes : int = Field(ge=0, max_digits=2)
    
class penalties_out(penalties_model):
    
    penaltie_id : UUID