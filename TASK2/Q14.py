import pandas as pd


matches = pd.read_csv("matches.csv")


matches_per_season = matches['season'].value_counts().sort_index()

print("Total number of matches played in each season:")
print(matches_per_season)
