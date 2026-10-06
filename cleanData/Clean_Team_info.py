import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_team_info():
    print("Début clean up Team_info")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/team_info.csv")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Team")
    rapport_ligne.append("="*40 + "\n")

    df = df.drop(columns=['link'])

    rapport_ligne.append("aucun probleme à signaler dans le csv\n")
    rapport_ligne.append("seul la colonne link est retirer car inutile")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Team_Info.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_team_info()