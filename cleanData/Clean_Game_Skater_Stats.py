import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_donnee_Game_skater_stats():
    print("Début clean up Game_skater_stats")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_skater_stats.csv")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game_skater_stats")
    rapport_ligne.append("="*40 + "\n")

    initial_row = len(df)
    miss_value = df["hits"].isna().sum()
    rapport_ligne.append("on retire les colonnes 'hits', 'takeaways', 'giveaways' et 'blocked'")
    rapport_ligne.append(f"trop de donnée manquant : {miss_value} manquant ({round((miss_value/initial_row)*100,2)} %)")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Skater_Stats.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_donnee_Game_skater_stats()