import pandas as pd


matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")


runs_per_match = deliveries.groupby('match_id')['total_runs'].sum()
runs_per_match = runs_per_match.reset_index()


runs_per_match = runs_per_match.merge(matches[['id', 'venue']], left_on='match_id', right_on='id')


avg_runs_venue = runs_per_match.groupby('venue')['total_runs'].mean()

print("Average runs scored at each venue:")
print(avg_runs_venue)
