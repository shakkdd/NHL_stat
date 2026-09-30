import pandas as pd

df = pd.read_csv("DATA/game_goals.csv")

df["gameWinningGoal"] = df["gameWinningGoal"].astype(bool)
df["emptyNet"] = df["emptyNet"].astype(bool)

df.info()

#df.to_csv("CleanCSV/Clean_Game_Goals.csv", index=True, index_label="game_goals_id")