import pandas as pd

df = pd.read_csv("DATA/game_goalie_stats.csv")
rapport_Path = "cleanData/rapport_global_nettoyage.txt"

rapport_ligne = []

rapport_ligne.append("="*20)
rapport_ligne.append("Rapport sur CSV Game_goalie_stats")
rapport_ligne.append("="*20 + "\n")

initial_row = len(df)
rapport_ligne.append(f"nb ligne : {initial_row}")

rapport_ligne.append("suppresion de doublon")
df.drop_duplicates(inplace=True)

rapport_ligne.append("check des valeur null")
rapport_ligne.append("-"*20)
rapport_ligne.append(df.isna().sum().to_string())
rapport_ligne.append("pour les colonne Decision et powerPlaySavePercentage, les valeur null sont justifiable :")
rapport_ligne.append("Decision : Changement du gardien avant la fin du match")
rapport_ligne.append("powerPlaySavePercentage : aucun tir recu lorsque que l'équipe est en avantage numérix de joueur")
rapport_ligne.append("-"*20)
rapport_ligne.append("suppresion des ligne avec des valeur null pour les colonnes 'savePercentage' et 'evenStrengthSavePercentage'")

df.dropna(subset=["evenStrengthSavePercentage", "savePercentage"], inplace=True)

rapport_ligne.append(f"ligne restant : {len(df)}")

with open(rapport_Path, "a", encoding="UTF-8") as f:
    f.write("\n".join(rapport_ligne))
    
#df.to_csv("CleanCSV/Clean_Game_Goalie_Stats.csv", index=False)