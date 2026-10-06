import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyage_donnee_Game_penaltie():
    print("Début clean up Game_penaltie")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_penalties.csv")

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game_penalties")
    rapport_ligne.append("="*40 + "\n")

    rapport_ligne.append("penalité vide : "+str(df["penaltySeverity"].isna().sum()))
    rapport_ligne.append(
    """
    beaucoup de ligne ont des 'Penalty_severity' non remplit

    de plus certaine pénalité pour 'Game Misconduct' resulte en une pénalité de 0 minutes
    or dans les regles les pénalité pour 'Game misconduct' est toujours de 10 minute

    la 'penaltySeverity' peu etre trouver par rapport à 'penaltyMinutes' :
    0 ==> Penalty shot
    2 ==> Minor or Bench Minor
    4 ==> Minor
    5 ==> Major
    10 ==> Game Misconduct or Misconduct

    nous utiliseront :
    2 minutes penalty : Minor penaltie par défaut
    10 minutes penalty : Game Misconduct âr défault
    """
    )

    def penaltyTypeUpdate(row):
        penaltyMin = row["penaltyMinutes"]
        
        if pd.isna(row["penaltySeverity"]):
            match penaltyMin:
                case 0:
                    row["penaltySeverity"] = "Penalty Shot"
                case 2 | 4:  
                    row["penaltySeverity"] = "Minor"
                case 5:
                    row["penaltySeverity"] = "Major"
                case 10:
                    row["penaltySeverity"] = "Game Misconduct"
                    
        return row["penaltySeverity"]

    def penaltyMinUpdate(row):
        penaltyMin = row["penaltyMinutes"]
        penaltySev = row["penaltySeverity"]
        
        if penaltySev == "Game Misconduct" and penaltyMin ==0:
            row["penaltyMinutes"] = 10
        
        return row["penaltyMinutes"]
                    
    df["penaltySeverity"] = df.apply(penaltyTypeUpdate, axis=1)
    df["penaltyMinutes"] = df.apply(penaltyMinUpdate, axis=1)

    rapport_ligne.append("penalité vide : "+ str(df["penaltySeverity"].isna().sum()))
    rapport_ligne.append("plus aucun valeur vide")

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Penaltie.csv", index=False)
    
if __name__ == "__main__":
    nettoyage_donnee_Game_penaltie()