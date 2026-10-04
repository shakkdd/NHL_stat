import pandas as pd

df = pd.read_csv("DATA/game_scratches.csv")

df .info()

#df.to_csv("CleanCSV/Clean_Game_Scratches.csv", index=False)