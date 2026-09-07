import pandas as pd


deliveries = pd.read_csv("deliveries.csv")




not_bowler_wicket = ['run out', 'retired hurt', 'obstructing the field']

wickets_df = deliveries[deliveries['player_dismissed'].notnull()]
wickets_df = wickets_df[~wickets_df['dismissal_kind'].isin(not_bowler_wicket)]

wickets_per_bowler = wickets_df.groupby('bowler')['player_dismissed'].count()
wickets_per_bowler = wickets_per_bowler.sort_values(ascending=False)

print("Total wickets taken by each bowler:")
print(wickets_per_bowler)
