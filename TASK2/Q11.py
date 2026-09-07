import pandas as pd


deliveries = pd.read_csv("deliveries.csv")


sixes = deliveries[deliveries['batsman_runs'] == 6]

print("Total deliveries where a six was scored =", len(sixes))
print(sixes[['match_id', 'batsman', 'batsman_runs']])
