import pandas as pd


deliveries = pd.read_csv("deliveries.csv")


runs_per_batsman = deliveries.groupby('batsman')['batsman_runs'].sum()
top_10_batsman = runs_per_batsman.sort_values(ascending=False).head(10)

print("Top 10 run scorers:")
print(top_10_batsman)
