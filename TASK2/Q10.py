import pandas as pd


matches = pd.read_csv("matches.csv")


pom_counts = matches['player_of_match'].value_counts()
pom_more_than_3 = pom_counts[pom_counts > 3]

print("Players with more than 3 Player of the Match awards:")
print(pom_more_than_3)
