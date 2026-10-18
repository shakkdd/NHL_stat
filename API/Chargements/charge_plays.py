import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_play():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Plays.csv")
    
    ligne = [
        {
            "play_id" : valeur_texte(ligne["play_id"]),
            "game_id" : valeur_texte(ligne["game_id"]),
            "for_team_id" : valeur_texte(ligne["team_id_for"]),
            "against_team_id" : valeur_texte(ligne["team_id_against"]),
            "event" : valeur_texte(ligne["event"]),
            "secondary_type" : valeur_texte(ligne["secondaryType"]),
            "x" : valeur_entier(ligne["x"]),
            "y" : valeur_entier(ligne["y"]),
            "period" : valeur_texte(ligne["period"]),
            "period_type" : valeur_texte(ligne["periodType"]),
            "period_time" : valeur_entier(ligne["periodTime"]),
            "period_time_remaining" : valeur_entier(ligne["periodTimeRemaining"]),
            "date_time" : ligne["dateTime"],
            "goals_away" : valeur_entier(ligne["goals_away"]),
            "goals_home" : valeur_entier(ligne["goals_home"]),
            "description": valeur_texte(ligne["description"]),
            "st_x" : valeur_entier(ligne["st_x"]),
            "st_y" : valeur_entier(ligne["st_y"])
        }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO public."Plays"(
            play_id,
            game_id,
            for_team_id,
            against_team_id,
            event,
            secondary_type,
            x,
            y,
            period,
            period_type,
            period_time,
            period_time_remaining,
            date_time,
            goals_away,
            goals_home,
            description,
            st_x,
            st_y
        )
        VALUES(
            :play_id,
            :game_id,
            :for_team_id,
            :against_team_id,
            :event,
            :secondary_type,
            :x,
            :y,
            :period,
            :period_type,
            :period_time,
            :period_time_remaining,
            :date_time,
            :goals_away,
            :goals_home,
            :description,
            :st_x,
            :st_y
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Plays", requete, ligne, [])
    finally:
        engine.dispose()

if __name__ == "__main__":
    insert_play()