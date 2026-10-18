import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_shift():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Shifts.csv")
    
    ligne = [
        {
            "game_id" : valeur_texte(ligne["game_id"]),
            "player_id" : valeur_texte(ligne["player_id"]),
            "period" : valeur_entier(ligne["period"]),
            "shift_start" : ligne["shift_start"],
            "shift_end" : ligne["shift_end"]
        }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
       INSERT INTO public."Game_Shifts"(
           game_id,
           player_id,
           period,
           shift_start,
           shift_end
       )
       VALUES(
           :game_id,
           :player_id,
           :period,
           :shift_start,
           :shift_end
       )
    """
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Game_Shifts", requete, ligne,[])
    finally:
        engine.dispose()

if __name__ == "__main__":
    insert_shift()