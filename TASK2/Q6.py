import pandas as pd


matches = pd.read_csv("matches.csv")


tie_matches = matches[matches['result'] == 'tie']

print("Matches where the result was a tie:")
print(tie_matches[['team1', 'team2', 'winner']])
