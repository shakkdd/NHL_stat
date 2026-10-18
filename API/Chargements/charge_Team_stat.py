import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_team_stat():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Team_Stats.csv")
    
    ligne = [
        {
            "game_id" : valeur_texte(ligne["game_id"]),
            "team_id" : valeur_texte(ligne["team_id"]),
            "hoa" : valeur_texte(ligne["HoA"]),
            "won" : ligne["won"],
            "settled_in" : valeur_texte(ligne["settled_in"]),
            "head_coach" : valeur_texte(ligne["head_coach"]),
            "goals" : valeur_entier(ligne["goals"]),
            "shots" : valeur_entier(ligne["shots"]),
            "pim" : valeur_entier(ligne["pim"]),
            "power_play_opportunities" : valeur_entier(ligne["powerPlayOpportunities"]),
            "power_play_goals" : valeur_entier(ligne["powerPlayGoals"]),
            "face_off_win_percentage" : valeur_entier(ligne["faceOffWinPercentage"])
        }for ligne in df.to_dict(orient="records")
    ]

    requete = """
        INSERT INTO public."Game_team_stats"(
            game_id,
            team_id,
            hoa,
            won,
            settled_in,
            head_coach,
            goals,
            shots,
            pim,
            power_play_opportunities,
            power_play_goals,
            face_off_win_percentage
        )
        VALUES(
            :game_id,
            :team_id,
            :hoa,
            :won,
            :settled_in,
            :head_coach,
            :goals,
            :shots,
            :pim,
            :power_play_opportunities,
            :power_play_goals,
            :face_off_win_percentage
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Game_team_stats", requete, ligne, [])
    finally:
        engine.dispose()
    
if __name__ == "__main__":
    insert_team_stat()