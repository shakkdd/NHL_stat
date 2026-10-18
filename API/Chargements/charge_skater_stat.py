import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_skater_stat():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Skater_Stats.csv")
    
    ligne = [
        {
            "game_id" : valeur_texte(ligne["game_id"]),
            "player_id" : valeur_texte(ligne["player_id"]),
            "team_id" : valeur_texte(ligne["team_id"]),
            "time_on_ice": valeur_entier(ligne["timeOnIce"]),
            "assists": valeur_entier(ligne["assists"]),
            "goals" : valeur_entier(ligne["goals"]),
            "shots" : valeur_entier(ligne["shots"]) ,
            "power_play_goals" : valeur_entier(ligne["powerPlayGoals"]),
            "power_play_assists" : valeur_entier(ligne["powerPlayAssists"]),
            "penalty_minutes" : valeur_entier(ligne["penaltyMinutes"]),
            "face_off_wins" : valeur_entier(ligne["faceOffWins"]),
            "face_off_taken" : valeur_entier(ligne["faceoffTaken"]),
            "short_handed_goals" : valeur_entier(ligne["shortHandedGoals"]),
            "short_handed_assists" : valeur_entier(ligne["shortHandedAssists"]),
            "plus_minus" : valeur_entier(ligne["plusMinus"]),
            "even_time_on_ice" : valeur_entier(ligne["evenTimeOnIce"]),
            "short_handed_time_on_ice" : valeur_entier(ligne["shortHandedTimeOnIce"]),
            "power_play_time_on_ice" : valeur_entier(ligne["powerPlayTimeOnIce"])
        }for ligne in df.to_dict(orient="records")
    ]

    requete = """
        INSERT INTO public."Game_skater_stats"(
            game_id,
            player_id,
            team_id,
            time_on_ice,
            assists,
            goals,
            shots,
            power_play_goals,
            power_play_assists,
            penalty_minutes,
            face_off_wins,
            face_off_taken,
            short_handed_goals,
            short_handed_assists,
            plus_minus,
            even_time_on_ice,
            short_handed_time_on_ice,
            power_play_time_on_ice         
        )
        VALUES(
            :game_id,
            :player_id,
            :team_id,
            :time_on_ice,
            :assists,
            :goals,
            :shots,
            :power_play_goals,
            :power_play_assists,
            :penalty_minutes,
            :face_off_wins,
            :face_off_taken,
            :short_handed_goals,
            :short_handed_assists,
            :plus_minus,
            :even_time_on_ice,
            :short_handed_time_on_ice,
            :power_play_time_on_ice
        )
    """
    
    try :
        with engine.begin() as conn:
            inserer_lots(conn, "Game_skater_stats", requete, ligne, [])
    finally:
        engine.dispose()

if __name__ == "__main__":
    insert_skater_stat()