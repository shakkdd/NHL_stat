import pandas as pd
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("CLEAN_DATA_PATH")

def change_id_to_uuid():
    print("début changement ID vers UUID")    
    
    df_game = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Game.csv")
    df_player = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Player_Info.csv")
    df_team = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Team_Info.csv")
    df_play = pd.read_csv(f"{DATA_DIR_INPUT}//Clean_Game_Plays.csv")

    game_map = {
        old_id : str(uuid.uuid4()) for old_id in df_game["game_id"]
    }

    player_map = {
        old_id : str(uuid.uuid4()) for old_id in df_player["player_id"]
    }

    team_map = {
        old_id : str(uuid.uuid4()) for old_id in df_team["team_id"]
    }

    play_map = {
        old_id : str(uuid.uuid4()) for old_id in df_play["play_id"]
    }

    # chagement des ID table "Principal"
    df_game["game_id"] = df_game["game_id"].map(game_map)
    
    df_player["player_id"] = df_player["player_id"].map(player_map)
    df_player.to_csv(f"{DATA_DIR_INPUT}/Clean_Player_Info.csv", index=False)

    df_team["team_id"] = df_team["team_id"].map(team_map)
    df_team.to_csv(f"{DATA_DIR_INPUT}/Clean_Team_Info.csv", index=False)

    df_play["play_id"] = df_play["play_id"].map(play_map)

    #changer les id dans les autre tables
    """
    Changement dans la table Plays
    For_team_id
    against_team_id
    """
    df_play["team_id_for"] = df_play["team_id_for"].map(team_map)
    df_play["team_id_against"] = df_play["team_id_against"].map(team_map)
    
    df_play.to_csv(f"{DATA_DIR_INPUT}//Clean_Game_Plays.csv", index=False)

    """
    Changement dans la table Penalties
    play_id
    """
    df_penalties = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Game_Penaltie.csv")
    df_penalties["play_id"] = df_penalties["play_id"].map(play_map)
    
    df_penalties.to_csv(f"{DATA_DIR_INPUT}/Clean_Game_Penaltie.csv", index=False)


    """
    Changement dans la table Game
    away_team_id
    home_team_id
    """
    df_game["away_team_id"] = df_game["away_team_id"].map(team_map)
    df_game["home_team_id"] = df_game["home_team_id"].map(team_map)
    
    df_game.to_csv(f"{DATA_DIR_INPUT}/Clean_Game.csv", index=False)

    """
    Changement dans la table Game_team_stat
    team_id
    game_id
    """
    df_game_team_stat = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Game_Team_Stats.csv")
    df_game_team_stat["game_id"] = df_game_team_stat["game_id"].map(game_map)
    df_game_team_stat["team_id"] = df_game_team_stat["team_id"].map(team_map)
    
    df_game_team_stat.to_csv(f"{DATA_DIR_INPUT}/Clean_Game_Team_Stats.csv", index=False)

    """
    Changement dans la table Game_goalie_stats
    team_id
    game_id
    player_id
    """

    df_game_goalie_stats = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Game_Goalie_Stats.csv")
    df_game_goalie_stats["game_id"] = df_game_goalie_stats["game_id"].map(game_map)
    df_game_goalie_stats["team_id"] = df_game_goalie_stats["team_id"].map(team_map)
    df_game_goalie_stats["player_id"] = df_game_goalie_stats["player_id"].map(player_map)
    
    df_game_goalie_stats.to_csv(f"{DATA_DIR_INPUT}/Clean_Game_Goalie_Stats.csv", index=False)

    """
    Changement dans la table Game_skater_stats
    team_id
    game_id
    player_id
    """
    df_game_skater_stats = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Game_Skater_Stats.csv")
    df_game_skater_stats["game_id"] = df_game_skater_stats["game_id"].map(game_map)
    df_game_skater_stats["team_id"] = df_game_skater_stats["team_id"].map(team_map)
    df_game_skater_stats["player_id"] = df_game_skater_stats["player_id"].map(player_map)
    
    df_game_skater_stats.to_csv(f"{DATA_DIR_INPUT}/Clean_Game_Skater_Stats.csv", index=False)

    """
    Changement dans la table Game_shift
    player_id
    game_id
    """
    df_shift = pd.read_csv(f"{DATA_DIR_INPUT}//Clean_Game_Shifts.csv")
    df_shift["game_id"] = df_shift["game_id"].map(game_map)
    df_shift["player_id"] = df_shift["player_id"].map(player_map)
    
    df_shift.to_csv(f"{DATA_DIR_INPUT}//Clean_Game_Shifts.csv", index=False)

    """
    changement dans la table Game_play_player
    player_id
    game_id
    play_id
    """
    df_game_play_player = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Game_Plays_Players.csv")
    df_game_play_player["play_id"] = df_game_play_player["play_id"].map(play_map)
    df_game_play_player["player_id"] = df_game_play_player["player_id"].map(player_map)
    df_game_play_player["game_id"] = df_game_play_player["game_id"].map(game_map)
    
    df_game_play_player.to_csv(f"{DATA_DIR_INPUT}/Clean_Game_Plays_Players.csv", index=False)
    
    """
    Changement dans la table Goals
    """
    df_game_goals = pd.read_csv(f"{DATA_DIR_INPUT}/Clean_Game_Goals.csv")
    df_game_goals["play_id"] = df_game_goals["play_id"].map(play_map)
    goals_map = {
        old_id : str(uuid.uuid4()) for old_id in df_game_goals["goals_id"]
    }
    df_game_goals["goals_id"] = df_game_goals["goals_id"].map(goals_map)
    
    df_game_goals.to_csv(f"{DATA_DIR_INPUT}/Clean_Game_Goals.csv", index=False)