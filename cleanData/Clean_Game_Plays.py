import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_donnee_Game_plays():
    print("Début clean up Game_play")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_plays.csv")

    df["team_id_for"] = df["team_id_for"].astype("Int64")
    df["team_id_against"] = df["team_id_against"].astype("Int64")
    df["x"] = df["x"].astype("Int64")
    df["y"] = df["y"].astype("Int64")
    df["periodTimeRemaining"] = df["periodTimeRemaining"].astype("Int64")
    df["st_x"] = df["st_x"].astype("Int64")
    df["st_y"] = df["st_y"].astype("Int64")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game_plays")
    rapport_ligne.append("="*40 + "\n")

    initial_row = len(df)

    rapport_ligne.append(f"ligne initiale : {initial_row}")

    df.drop_duplicates(inplace=True)
    rapport_ligne.append(f"supression des doublon : {initial_row - len(df)}")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Plays.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_donnee_Game_plays()