import pandas as pd

df = pd.read_csv("DATA/game_plays_players.csv")

df.info()

#df.to_csv("Clean/Clean_Game_Plays_Players.csv", index=False)