import pandas as pd

df = pd.read_csv("DATA/player_info.csv")

df["weight"] = df["weight"].astype("Int64")

df.info()

#df.to_csv(path_or_buf="./CleanCSV/Clean_Player_Info.csv", index=False)