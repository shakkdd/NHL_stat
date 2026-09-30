import pandas as pd

df = pd.read_csv("DATA/game.csv")

df = df.drop(columns=["venue_link"])

df.info()

#df.to_csv("CleanCSV/Clean_Game.csv", index=False)