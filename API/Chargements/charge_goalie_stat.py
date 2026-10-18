import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from API.Chargements.chargement import valeur_texte, valeur_entier, valeur_decimal, inserer_lots

load_dotenv()

url = os.getenv("DB_PATH")
engine = create_engine(f"postgresql+psycopg2://{os.getenv("DB_PATH")}")

def insert_goalies_stats():
    DIR_PATH = os.getenv("CLEAN_DATA_PATH")
    df = pd.read_csv(f"{DIR_PATH}/Clean_Game_Goalie_Stats.csv")
    
    ligne = [
        {
            "game_id" : valeur_texte(ligne["game_id"]),
            "player_id": valeur_texte(ligne["player_id"]),
            "team_id" : valeur_texte(ligne["team_id"]),
            "time_on_ice" : valeur_entier(ligne["timeOnIce"]),
            "assists" : valeur_entier(ligne["assists"]),
            "goals" : valeur_entier(ligne["goals"]),
            "pim" : valeur_entier(ligne["pim"]),
            "shots" : valeur_entier(ligne["shots"]),
            "saves" : valeur_entier(ligne["saves"]),
            "power_play_saves" : valeur_entier(ligne["powerPlaySaves"]) ,
            "short_handed_saves" : valeur_entier(ligne["shortHandedSaves"]),
            "even_save" : valeur_entier(ligne["evenSaves"]),
            "short_handed_shots_against" : valeur_entier(ligne["shortHandedShotsAgainst"]),
            "even_shots_against" : valeur_entier(ligne["evenShotsAgainst"]),
            "power_play_shots_against" : valeur_entier(ligne["powerPlayShotsAgainst"]),
            "decision" : valeur_texte(ligne["decision"]),
            "save_percentage" : valeur_decimal(ligne["savePercentage"]),
            "power_play_saves_percentage" : valeur_decimal(ligne["powerPlaySavePercentage"]),
            "even_strenght_save_percentage" : valeur_decimal(ligne["evenStrengthSavePercentage"])
        }for ligne in df.to_dict(orient="records")
    ]
    
    requete = """
        INSERT INTO public."Game_goalie_stats"(
            game_id,
            player_id,
            team_id,
            time_on_ice,
            assists,
            goals,
            pim,
            shots,
            saves,
            power_play_saves,
            short_handed_saves,
            even_save,
            short_handed_shots_against,
            even_shots_against,
            power_play_shots_against,
            decision,
            save_percentage,
            power_play_saves_percentage,
            even_strenght_save_percentage
        )VALUES(
            :game_id,
            :player_id,
            :team_id,
            :time_on_ice,
            :assists,
            :goals,
            :pim,
            :shots,
            :saves,
            :power_play_saves,
            :short_handed_saves,
            :even_save,
            :short_handed_shots_against,
            :even_shots_against,
            :power_play_shots_against,
            :decision,
            :save_percentage,
            :power_play_saves_percentage,
            :even_strenght_save_percentage
        )
    """
    
    try:
        with engine.begin() as conn:
            inserer_lots(conn, "Game_goalie_stats", requete, ligne,[])
    finally:
        engine.dispose()
        
if __name__ == "__main__":
    insert_goalies_stats()