from pydantic import BaseModel, Field

class Game_skater_stats_Model(BaseModel):
    player_id : str = Field(max_length=7)
    team_id : int = Field(max_digits=3)
    timeOnIce : int
    assists : int
    goals : int
    shots : int
    hits : int
    powerPlayGoals : int
    powerPlayAssists : int
    penaltyMinutes : int
    faceOffWins : int
    faceoffTaken : int
    takeaways : int
    giveaways : int
    shortHandedGoals : int
    shortHandedAssists : int
    blocked : int
    plusMinus : int
    evenTimeOnIce : int
    shortHandedTimeOnIce : int
    powerPlayTimeOnIce : int
    
class Game_skater_stats_Out(Game_skater_stats_Model):
    game_id : int