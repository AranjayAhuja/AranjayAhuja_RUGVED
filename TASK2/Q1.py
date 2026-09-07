import pandas as pd


matches = pd.read_csv("matches.csv")


matches_2008 = matches[matches['season'] == 2008]

print("Total number of matches conducted in 2008 =", len(matches_2008))
