import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_decimal,inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_player():
    print("insertion player")
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Player_info.csv")
    
    ligne = [{
        "player_id" : valeur_texte(ligne["player_id"]),
        "first_name" : valeur_texte(ligne["firstName"]),
        "last_name" : valeur_texte(ligne["lastName"]),
        "nationality" : valeur_texte(ligne["nationality"]),
        "birth_city" : valeur_texte(ligne["birthCity"]),
        "primary_position": valeur_texte(ligne["primaryPosition"]),
        "birth_date" : ligne["birthDate"],
        "height": valeur_texte(ligne["height"]),
        "height_cm" : valeur_decimal(ligne["height_cm"]),
        "weight" : valeur_decimal(ligne["weight"]),
        "shoots_catches" : valeur_texte(ligne["shootsCatches"])
    }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO "Players"(
            player_id,
            first_name,
            last_name,
            nationality,
            birth_city,
            primary_position,
            birth_date,
            height,
            height_cm,
            weight,
            shoots_catches
        )
        VALUES(
            :player_id,
            :first_name,
            :last_name,
            :nationality,
            :birth_city,
            :primary_position,
            :birth_date,
            :height,
            :height_cm,
            :weight,
            :shoots_catches
        )
    """
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Players", requete, ligne,[])
    finally:
        engine.dispose()
if __name__ == "__main__":
    insert_player()