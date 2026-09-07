import pandas as pd


matches = pd.read_csv("matches.csv")

toss_tally = matches.groupby(['toss_winner', 'toss_decision']).size()

print("Toss decisions taken by each team:")
print(toss_tally)
