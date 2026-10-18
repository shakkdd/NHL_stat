import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, inserer_lots

load_dotenv()


url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")


def insert_Game():
    print("insertion Game")
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game.csv", dtype={
        "season": str,
        "game_id" : str,       
        })
    
    ligne = [{
        "game_id" : valeur_texte(ligne["game_id"]),
        "season": valeur_texte(ligne["season"]),
        "type" : valeur_texte(ligne["type"]),
        "date_time" : ligne["date_time_GMT"],
        "away_team_id" : valeur_texte(ligne["away_team_id"]),
        "home_team_id" : valeur_texte(ligne["home_team_id"]),
        "away_goals": valeur_entier(ligne["away_goals"]),
        "home_goals": valeur_entier(ligne["home_goals"]),
        "outcome": valeur_texte(ligne["outcome"]),
        "venue": valeur_texte(ligne["venue"]),
        "venue_time_zone": valeur_texte(ligne["venue_time_zone_id"]),
        "venue_time_zone_offset": valeur_entier(ligne["venue_time_zone_offset"]),
        "venue_time_zone_tz": valeur_texte(ligne["venue_time_zone_tz"])
    }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO public."Games"(
            game_id,
            season,
            type,
            date_time,
            away_team_id,
            home_team_id,
            away_goals,
            home_goals,
            outcome,
            venue,
            venue_time_zone,
            venue_time_zone_offset,
            venue_time_zone_tz
        )
        VALUES(
            :game_id,
            :season,
            :type,
            :date_time,
            :away_team_id,
            :home_team_id,
            :away_goals,
            :home_goals,
            :outcome,
            :venue,
            :venue_time_zone,
            :venue_time_zone_offset,
            :venue_time_zone_tz
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Games", requete, ligne,[])
    finally:
        engine.dispose()

if __name__ == "__main__":
    insert_Game()