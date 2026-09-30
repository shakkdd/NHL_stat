import pandas as pd

df = pd.read_csv("DATA/game_skater_stats.csv")

df["hits"] = df["hits"].astype("Int64")
df["takeaways"] = df["takeaways"].astype("Int64")
df["giveaways"] = df["giveaways"].astype("Int64")
df["blocked"] = df["blocked"].astype("Int64")

df.info()
#df.to_csv("CleanCSV/Clean_Game_Skater_Stats.csv", index=False)