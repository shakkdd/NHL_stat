import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def nettoyer_donnees_Game_team_stats():
    print("Début clean up Game_team_stats")
    """
    Fonction principale pour nettoyer les statistiques des équipes par match.
    Elle supprime les doublons, fusionne les données de score et de joueurs,
    et génère un fichier propre ainsi qu'un rapport de nettoyage.
    """
    # 1. Chargement des fichiers CSV
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_teams_stats.csv")
    df_game = pd.read_csv(f"{DATA_DIR_INPUT}/game.csv")
    df_skater = pd.read_csv(f"{DATA_DIR_INPUT}/game_skater_stats.csv")

    # Suppression des doublons de base
    df = df.drop_duplicates()
    df_game = df_game.drop_duplicates()

    # Garder une trace du nombre de lignes de départ
    lignes_depart = len(df)

    # 2. Remplacement des valeurs manquantes pour le coach
    df["head_coach"] = df["head_coach"].fillna("Inconnu")

    # 3. Récupération des buts officiels depuis game.csv
    # On sépare les équipes à domicile et à l'extérieur pour les regrouper
    domicile = df_game[["game_id", "home_team_id", "home_goals"]].rename(
        columns={"home_team_id": "team_id", "home_goals": "official_goals"}
    )
    exterieur = df_game[["game_id", "away_team_id", "away_goals"]].rename(
        columns={"away_team_id": "team_id", "away_goals": "official_goals"}
    )
    scores_officiels = pd.concat([domicile, exterieur], ignore_index=True)

    # Fusion avec les scores officiels
    df = df.merge(scores_officiels, on=["game_id", "team_id"], how="left")

    # Comptage pour le rapport
    nb_buts_manquants = int(df["goals"].isna().sum())
    nb_buts_corriges = int((df["goals"].notna() & df["goals"].ne(df["official_goals"])).sum())

    # Remplacement des buts par les scores officiels
    df["goals"] = df["official_goals"]
    df = df.drop(columns=["official_goals"])

    # 4. Calcul des totaux des joueurs (skaters) pour compléter les tirs et pénalités
    totaux_skaters = df_skater.groupby(["game_id", "team_id"])[
        ["shots", "penaltyMinutes", "faceOffWins", "faceoffTaken"]
    ].sum().reset_index()

    totaux_skaters = totaux_skaters.rename(columns={
        "shots": "shots_skaters",
        "penaltyMinutes": "pim_skaters",
        "faceOffWins": "fc_wins",
        "faceoffTaken": "fc_taken"
    })

    # Fusion avec le fichier principal
    df = df.merge(totaux_skaters, on=["game_id", "team_id"], how="left")

    # Compléter les valeurs manquantes de tirs et PIM
    shots_avant = int(df["shots"].isna().sum())
    df["shots"] = df["shots"].fillna(df["shots_skaters"])
    shots_recuperes = shots_avant - int(df["shots"].isna().sum())

    pim_avant = int(df["pim"].isna().sum())
    df["pim"] = df["pim"].fillna(df["pim_skaters"])
    pim_recuperees = pim_avant - int(df["pim"].isna().sum())

    # 5. Calcul du pourcentage de mises au jeu si manquant
    calc_pourcentage = (100 * df["fc_wins"] / df["fc_taken"]).round(1)
    fc_avant = int(df["faceOffWinPercentage"].isna().sum())
    df["faceOffWinPercentage"] = df["faceOffWinPercentage"].fillna(calc_pourcentage)
    fc_recupere = fc_avant - int(df["faceOffWinPercentage"].isna().sum())

    # 6. Suppression des colonnes inutiles ou temporaires
    colonnes_a_supprimer = [
        "blocked", "takeaways", "giveaways", "hits", "startRinkSide",
        "shots_skaters", "pim_skaters", "fc_wins", "fc_taken"
    ]
    df = df.drop(columns=colonnes_a_supprimer)

    # Conversion de certaines colonnes en entiers
    colonnes_int = ["goals", "shots", "pim", "powerPlayOpportunities", "powerPlayGoals"]
    for col in colonnes_int:
        df[col] = df[col].astype("Int64")

    # 7. Création du rapport de nettoyage
    rapport = [
        "========================================\n",
        "Rapport sur le nettoyage de game_teams_stats\n",
        "========================================\n",
        f"Nombre de lignes initiales : {lignes_depart}\n",
        f"Colonnes inutiles retirées : {', '.join(colonnes_a_supprimer[:5])}\n",
        "",
        "Valeurs récupérées :",
        f"- Buts récupérés/corrigés : {nb_buts_manquants} (manquants) / {nb_buts_corriges} (corrigés)\n",
        f"- Tirs (shots) récupérés : {shots_recuperes}\n",
        f"- Minutes de pénalité (pim) récupérées : {pim_recuperees}\n",
        f"- Pourcentages de mises au jeu calculés : {fc_recupere}\n",
        "\n",
        "Valeurs manquantes restantes par colonne :\n"
    ]

    valeurs_manquantes = df.isna().sum()
    for col, val in valeurs_manquantes.items():
        if val > 0:
            rapport.append(f"- {col} : {val}\n")

    # 8. Sauvegarde des résultats
    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Team_Stats.csv", index=False)

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport)+"\n")

if __name__ == "__main__":
    nettoyer_donnees_Game_team_stats()