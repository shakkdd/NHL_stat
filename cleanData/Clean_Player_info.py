import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_player_info():
    print("début clean up Player_info")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/player_info.csv")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game")
    rapport_ligne.append("="*40 + "\n")

    df["weight"] = df["weight"].astype("Int64")
    df = df.drop(columns="birthStateProvince")

    rapport_ligne.append("retire la collone 'birthStateProvince' car non utile")

    rapport_ligne.append("aucune ligne apparait en double")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Player_Info.csv", index=False)

if __name__ == "__main__":
    nettoyage_player_info()