import pandas as pd

df = pd.read_csv("DATA/game_teams_stats.csv")

df["goals"] = df["goals"].astype("Int64")
df["shots"] = df["shots"].astype("Int64")
df["hits"] = df["hits"].astype("Int64")
df["pim"] = df["pim"].astype("Int64")
df["powerPlayOpportunities"] = df["powerPlayOpportunities"].astype("Int64")
df["powerPlayGoals"] = df["powerPlayGoals"].astype("Int64")
df["giveaways"] = df["giveaways"].astype("Int64")
df["takeaways"] = df["takeaways"].astype("Int64")
df["blocked"] = df["blocked"].astype("Int64")

df.info()
#df.to_csv("CleanCSV/Clean_Game_Team_Stats.csv", index=False)