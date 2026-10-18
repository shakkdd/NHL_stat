import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR_INPUT = os.getenv("DATA_PATH")
DATA_DIR_OUTPUT = os.getenv("CLEAN_DATA_PATH")
RAPPORT_PATH = os.getenv("REPORT_PATH")

def update_time_remaining(row: pd.Series, game_type: str | None = None) -> int | None:
    if pd.notna(row["periodTimeRemaining"]):
        return int(row["periodTimeRemaining"])

    if pd.isna(row["periodTime"]):
        return None

    period_type = str(row["periodType"]).strip().upper()
    if period_type == "REGULAR":
        period_duration = 1200
    elif period_type == "OVERTIME":
        normalized_game_type = str(game_type).strip().upper()
        if normalized_game_type == "R":
            period_duration = 300
        elif normalized_game_type == "P":
            period_duration = 1200
        else:
            return None
    elif period_type == "SHOOTOUT":
        period_duration = 300
    else:
        return None

    return period_duration - int(row["periodTime"])

def nettoyage_donnee_Game_plays():
    print("Début clean up Game_play")
    df = pd.read_csv(f"{DATA_DIR_INPUT}/game_plays.csv")
    initial_row = len(df)

    df["team_id_for"] = df["team_id_for"].astype("Int64")
    df["team_id_against"] = df["team_id_against"].astype("Int64")
    df["x"] = df["x"].astype("Int64")
    df["y"] = df["y"].astype("Int64")
    df["periodTimeRemaining"] = df["periodTimeRemaining"].astype("Int64")
    df["st_x"] = df["st_x"].astype("Int64")
    df["st_y"] = df["st_y"].astype("Int64")

    games = pd.read_csv(f"{DATA_DIR_INPUT}/game.csv", usecols=["game_id", "type"])
    conflicting_game_types = games.groupby("game_id")["type"].nunique()
    if conflicting_game_types.gt(1).any():
        raise ValueError("game.csv contient plusieurs types pour un même game_id.")
    game_types = games.drop_duplicates(subset=["game_id"]).set_index("game_id")["type"]
    missing_time = df["periodTimeRemaining"].isna()
    missing_time_count = int(missing_time.sum())
    if missing_time.any():
        df.loc[missing_time, "periodTimeRemaining"] = df.loc[missing_time].apply(
            lambda row: update_time_remaining(
                row, game_types.get(row["game_id"])
            ),
            axis=1,
        )

    calculated_time = missing_time & df["periodTimeRemaining"].notna()
    period_types = df["periodType"].astype("string").str.upper()
    game_types_by_play = df["game_id"].map(game_types).astype("string").str.upper()
    calculated_regular = int((calculated_time & period_types.eq("REGULAR")).sum())
    calculated_overtime_regular = int(
        (calculated_time & period_types.eq("OVERTIME") & game_types_by_play.eq("R")).sum()
    )
    calculated_overtime_playoffs = int(
        (calculated_time & period_types.eq("OVERTIME") & game_types_by_play.eq("P")).sum()
    )
    calculated_shootout = int((calculated_time & period_types.eq("SHOOTOUT")).sum())

    rapport_ligne = []
    rapport_ligne.append("="*40)
    rapport_ligne.append("Rapport sur CSV Game_plays")
    rapport_ligne.append("="*40 + "\n")

    rapport_ligne.append(f"Nombre de lignes initiales : {initial_row}")
    rapport_ligne.append(
        f"temps restants manquants avant calcul : {missing_time_count}"
    )
    rapport_ligne.append("temps restants calculés (avant suppression des doublons) :")
    rapport_ligne.append(f"- périodes REGULAR : {calculated_regular}")
    rapport_ligne.append(
        f"- OVERTIME en saison régulière (type R) : {calculated_overtime_regular}"
    )
    rapport_ligne.append(
        f"- OVERTIME en play-offs (type P) : {calculated_overtime_playoffs}"
    )
    rapport_ligne.append(f"- périodes SHOOTOUT : {calculated_shootout}")

    df.drop_duplicates(inplace=True)
    rapport_ligne.append(f"Nombre de doublons supprimés : {initial_row - len(df)}")
    rapport_ligne.append(
        "temps restants manquants après calcul et suppression des doublons : "
        f"{int(df['periodTimeRemaining'].isna().sum())}"
    )

    with open(RAPPORT_PATH, "a", encoding="UTF-8") as f:
        f.write("\n".join(rapport_ligne)+"\n")

    df.to_csv(f"{DATA_DIR_OUTPUT}/Clean_Game_Plays.csv", index=False)

if __name__ == "__main__":
    nettoyage_donnee_Game_plays()