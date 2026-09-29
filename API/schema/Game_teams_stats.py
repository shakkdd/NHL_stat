from pydantic import BaseModel, Field

class game_teams_stats_Model(BaseModel):
    team_id : str = Field(max_length=10)
    HoA : str = Field(max_length=5)
    won : bool
    settled_in : str = Field(max_length=3)
    head_coach : str = Field(min_length=3)
    goals : int
    shot : int
    hits : int
    pim : int
    powerPlayOpportunities : int
    powerPlayGoals : int
    faceOffWinPercentage : float
    giveaways : int
    takeaways : int
    blocked : int
    startRinkSide : str = Field(max_length=5)
    
class game_teams_stats_Out(game_teams_stats_Model):
    game_id : str