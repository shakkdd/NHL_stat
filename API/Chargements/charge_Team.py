import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_team():
    print("insertion Teams")
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Team_info.csv")
    
    ligne = [{
        "team_id" : valeur_texte(ligne["team_id"]),
        "short_name" : valeur_texte(ligne["shortName"]),
        "team_name" : valeur_texte(ligne["teamName"]),
        "abbreviation" : valeur_texte(ligne["abbreviation"])
    }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO public."Teams"(
            team_id,
            short_name,
            team_name,
            abbreviation
        )
        VALUES(
            :team_id,
            :short_name,
            :team_name,
            :abbreviation
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Teams", requete, ligne,[])
    finally:
        engine.dispose()
    

if __name__ == "__main__":
    insert_team()