import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_goals():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Goals.csv")
    
    ligne = [
        {
            "goals_id" : valeur_texte(ligne["goals_id"]),
            "play_id" : valeur_texte(ligne["play_id"]),
            "strength" : valeur_texte(ligne["strength"]),
            "game_winning_goals" : ligne["gameWinningGoal"],
            "empty_net" : ligne["emptyNet"]
        }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO public.goals(
            goals_id,
            play_id,
            strength,
            game_winning_goals,
            empty_net
        )
        VALUES(
            :goals_id,
            :play_id,
            :strength,
            :game_winning_goals,
            :empty_net
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "goals", requete, ligne, [])
    finally:
        engine.dispose()

if __name__ == "__main__":
    insert_goals()