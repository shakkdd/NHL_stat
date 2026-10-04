import pandas as pd

df = pd.read_csv("DATA/game_shifts.csv")

df["shift_end"] = df["shift_end"].astype("Int64")

df.info()

#df.to_csv("CleanCSV/Clean_Game_Shifts.csv", index=False)