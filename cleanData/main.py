from change_id import change_id_to_uuid
from Clean_Game import nettoyage_donnee_Game
from Clean_Game_Goalie_Stats import nettoyage_donne_Game_goalie_stats
from Clean_Game_Goals import nettoyage_donnee_Game_goals
from Clean_Game_Penaltie import nettoyage_donnee_Game_penaltie
from Clean_Game_Plays import nettoyage_donnee_Game_plays
from Clean_Game_Plays_Players import nettoyage_donnee_Game_plays_player
from Clean_Game_Shifts import nettoyage_donnee_Game_shift
from Clean_Game_Skater_Stats import nettoyage_donnee_Game_skater_stats
from Clean_Game_Team_Stats import nettoyer_donnees_Game_team_stats
from Clean_Player_info import nettoyage_player_info
from Clean_Team_info import nettoyage_team_info

def main():
    print("Commencement de clean up csv")
    #Clean des csv de manière centraliser
    """Table principal"""
    nettoyage_player_info()
    nettoyage_team_info()
    nettoyage_donnee_Game()
    
    """table secondaire"""
    nettoyer_donnees_Game_team_stats()
    nettoyage_donnee_Game_plays()
    nettoyage_donnee_Game_plays_player()
    nettoyage_donnee_Game_shift()
    nettoyage_donnee_Game_penaltie()
    nettoyage_donnee_Game_goals()
    nettoyage_donne_Game_goalie_stats()
    nettoyage_donnee_Game_skater_stats()
    
    """Changement des ID par des UUID dans les CSV clean"""
    change_id_to_uuid()
    
if __name__ == "__main__":
    main()