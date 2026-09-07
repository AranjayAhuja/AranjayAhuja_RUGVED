import pandas as pd

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")




deliveries_season = deliveries.merge(matches[['id', 'season']], left_on='match_id', right_on='id')

runs_per_season = deliveries_season.groupby('season')['total_runs'].sum()

print("Total runs scored in each season:")
print(runs_per_season)
