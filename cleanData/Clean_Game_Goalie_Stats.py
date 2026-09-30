import pandas as pd

df = pd.read_csv("DATA/game_goalie_stats.csv")

df.info()

#df.to_csv("CleanCSV/Clean_Game_Goalie_Stats.csv", index=True, index_label="game_goalie_stats_id")