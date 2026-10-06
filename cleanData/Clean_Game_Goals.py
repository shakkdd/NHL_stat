import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")


def nettoyage_donnee_Game_goals():
    print("Début clean up Game_goals")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_goals.csv")
    df["gameWinningGoal"] = df["gameWinningGoal"].astype(bool)
    df["emptyNet"] = df["emptyNet"].astype(bool)

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game_goals")
    rapport_ligne.append("="*40 + "\n")

    rapport_ligne.append("Changement de type des colonne 'gameWinningGoal' et 'emptyNet' au type bool")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Goals.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_donnee_Game_goals()