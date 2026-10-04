import pandas as pd

df = pd.read_csv('DATA/game_penalties.csv')

df.info()

"""
many row doesn't have PenaltySeverity cell fill

we found out, some Game Misconduct penalty lead to 0 minute penalty
but Game Misconduct penalty always lead to 10 minute penalty

many penaltySeverity cell are empty
the penaltySeverity can be found by the penaltyMinutes
0 ==> Penalty shot
2 ==> Minor or Bench Minor
4 ==> Minor
5 ==> Major
10 ==> Game Misconduct or Misconduct

we will using for :
2 minutes penalty : Minor penaltie by default
10 minutes penalty : Game Misconduct by default
"""
def penaltyTypeUpdate(row):
    penaltyMin = row["penaltyMinutes"]
    
    if pd.isna(row["penaltySeverity"]):
        match penaltyMin:
            case 0:
                row["penaltySeverity"] = "Penalty Shot"
            case 2 | 4:  
                row["penaltySeverity"] = "Minor"
            case 5:
                row["penaltySeverity"] = "Major"
            case 10:
                row["penaltySeverity"] = "Game Misconduct"
                
    return row["penaltySeverity"]
                
df["penaltySeverity"] = df.apply(penaltyTypeUpdate, axis=1)

print(df.groupby(by=["penaltySeverity", "penaltyMinutes"]).agg(
    nb_penalty = ("penaltySeverity", "count")
))

#df.to_csv(path_or_buf="./CleanCSV/Clean_Game_Penaltie.csv", index=False)