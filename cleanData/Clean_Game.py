import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_donnee_Game():
    print("Début clean up Game")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game.csv")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game")
    rapport_ligne.append("="*40 + "\n")

    df = df.drop(columns=["venue_link", "home_rink_side_start"])
    rapport_ligne.append("on retire les colonne 'Venue_link' et 'home_rink_side_start' car non utile")

    initial_row = len(df)

    rapport_ligne.append("on retire les lignes en doublon")
    df.drop_duplicates(inplace=True)

    rapport_ligne.append(f"nombre de ligne supprimer : {initial_row-len(df)}")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_donnee_Game()