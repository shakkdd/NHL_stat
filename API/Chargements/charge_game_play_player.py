import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_player_play():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Plays_Players.csv")
    
    ligne = [
        {
            "play_id" : valeur_texte(ligne["play_id"]),
            "game_id" : valeur_texte(ligne["game_id"]),
            "player_id" : valeur_texte(ligne["player_id"]),
            "player_type" : valeur_texte(ligne["playerType"])
        }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO public."Game_play_players"(
            play_id,
            game_id,
            player_id,
            player_type
        )
        VALUES(
            :play_id,
            :game_id,
            :player_id,
            :player_type
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Game_play_players", requete, ligne, [])
    finally:
        engine.dispose()

if __name__ == "__main__":
    insert_player_play()