import pandas as pd


deliveries = pd.read_csv("deliveries.csv")



runs_per_batsman = deliveries.groupby('batsman')['batsman_runs'].sum()

dismissed = deliveries[deliveries['player_dismissed'].notnull()]
outs_per_batsman = dismissed.groupby('player_dismissed')['player_dismissed'].count()

batting_avg = runs_per_batsman / outs_per_batsman
batting_avg = batting_avg.dropna()
batting_avg = batting_avg.sort_values(ascending=False)

print("Top 10 batting averages:")
print(batting_avg.head(10))
