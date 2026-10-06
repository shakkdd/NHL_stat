import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_donnee_Game_plays_player():
    print("Début clean up Game_play_players")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_plays_players.csv")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game_plays_players")
    rapport_ligne.append("="*40 + "\n")

    initial_row = len(df)
    rapport_ligne.append(f"ligne : {initial_row}")

    df.drop_duplicates(inplace=True)

    rapport_ligne.append(f"ligne doublon supprimer : {initial_row - len(df)}")

    rapport_ligne.append("ligne vide : \n" + str(df.isna().sum()))

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Plays_Players.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_donnee_Game_plays_player()