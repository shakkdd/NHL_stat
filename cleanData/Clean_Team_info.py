import pandas as pd

df = pd.read_csv("DATA/team_info.csv")

df = df.drop(columns=['link'])

df.info()

#df.to_csv(path_or_buf="./CleanCSV/Clean_Team_Info.csv", index=False)