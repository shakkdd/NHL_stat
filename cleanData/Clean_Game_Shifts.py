import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_donnee_Game_shift():
    print("Début clean up Game_shift")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_shifts.csv")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game_plays")
    rapport_ligne.append("="*40 + "\n")


    df["shift_end"] = df["shift_end"].astype("Int64")

    initial_row = len(df)

    rapport_ligne.append(str(df["shift_end"].isna().sum()))
    rapport_ligne.append("supression des ligne vide")

    rapport_ligne.append(f"ligne supprimer : {initial_row - len(df)}")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Shifts.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_donnee_Game_shift()