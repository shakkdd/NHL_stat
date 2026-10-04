import pandas as pd

df = pd.read_csv("DATA/game_plays.csv")

df["team_id_for"] = df["team_id_for"].astype("Int64")
df["team_id_against"] = df["team_id_against"].astype("Int64")
df["x"] = df["x"].astype("Int64")
df["y"] = df["y"].astype("Int64")
df["periodTimeRemaining"] = df["periodTimeRemaining"].astype("Int64")
df["st_x"] = df["st_x"].astype("Int64")
df["st_y"] = df["st_y"].astype("Int64")

df.info()

#df.to_csv("CleanCSV/Clean_Game_Plays.csv", index=False)