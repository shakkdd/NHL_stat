import pandas as pd

df = pd.read_csv("DATA/game_officials.csv")

df.info()

#df.to_csv("CleanCSV/Clean_Game_Officials.csv", index=False, index_label="game_officials_id")