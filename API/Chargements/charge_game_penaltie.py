import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_penalties():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Penaltie.csv")
    
    ligne = [
        {
            "play_id" : valeur_texte(ligne["play_id"]),
            "penality_severity" : valeur_texte(ligne["penaltySeverity"]),
            "penalitie_minutes" : valeur_entier(ligne["penaltyMinutes"])
        }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO public."Penalities"(
            play_id,
            penality_severity,
            penalitie_minutes
        )
        VALUES(
            :play_id,
            :penality_severity,
            :penalitie_minutes
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Penalities", requete, ligne, [])
    finally:
        engine.dispose()

if __name__ == "__main__":
    insert_penalties()