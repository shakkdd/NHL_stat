from API.Chargements.charge_Game import insert_Game
from API.Chargements.charge_Player import insert_player
from API.Chargements.charge_Game_shift import insert_shift
from API.Chargements.charge_Team import insert_team
from API.Chargements.charge_goalie_stat import insert_goalies_stats
from API.Chargements.charge_skater_stat import insert_skater_stat
from API.Chargements.charge_Team_stat import insert_team_stat
from API.Chargements.charge_plays import insert_play
from API.Chargements.charge_game_goals import insert_goals
from API.Chargements.charge_game_penaltie import insert_penalties
from API.Chargements.charge_game_play_player import insert_player_play
import time

def insert_db():
    insert_team()
    insert_player()
    insert_Game()
    insert_play()
    insert_team_stat()
    insert_goalies_stats()
    insert_skater_stat()
    insert_shift()
    insert_goals()
    insert_penalties()
    insert_player_play()
    
if __name__ == "__main__":
    start = time.perf_counter()
    insert_db()
    end= time.perf_counter()
    execution_time = end- start
    print(f"Temps d'exécution : {execution_time:.4f} secondes")