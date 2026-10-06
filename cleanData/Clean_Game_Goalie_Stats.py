import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")


def nettoyage_donne_Game_goalie_stats():
    print("début clean up Game_goalie_stats")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_goalie_stats.csv")

    initial_row = len(df)
    df.drop_duplicates(inplace=True)
    after_drop_dup = len(df)
    

    df["decision"] = df["decision"].fillna("")
    df["powerPlaySavePercentage"] = df["powerPlaySavePercentage"].fillna(0)
        
    df["savePercentage"] = df["savePercentage"].fillna(
        df.groupby("player_id")["savePercentage"].transform("mean")
    )
    
    df["evenStrengthSavePercentage"] = df["evenStrengthSavePercentage"].fillna(
        df.groupby("player_id")["evenStrengthSavePercentage"].transform("mean")
    )
    
    df.dropna(inplace=True)
    
    rapport = [
        "="*20,
        "Rapport sur CSV Game_goalie_stats",
        "="*20 + "\n",
        f"nombre de ligne avant suppression des doublons : {initial_row}",
        f"nombre de ligne après suppression des doublons : {after_drop_dup}",
        "",
        "pour les colonne Decision et powerPlaySavePercentage, les valeur null sont justifiable :",
        "Decision : Changement du gardien avant la fin du match",
        "powerPlaySavePercentage : aucun tir recu lorsque que l'équipe est en avantage numérix de joueur",
        "remplisage des valeurs vide dans les colonne 'savePercentage' et 'evenStrengthSavePercentage'",
        "par la moyenne de ces colonne filtrer par le player_id",
        f"{df.isna().sum().to_string()}\n",
        "on drop les valeur manquant restant pour avoir un csv entierement clean"
    ]

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport)+"\n")
        
    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Goalie_Stats.csv", index=False)
        
   
if __name__ == "__main__":
    nettoyage_donne_Game_goalie_stats()