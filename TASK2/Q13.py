import pandas as pd


matches = pd.read_csv("matches.csv")


all_umpires = pd.concat([matches['umpire1'], matches['umpire2']])
umpire_counts = all_umpires.value_counts()

print("Umpire(s) who umpired the maximum number of times:")
print(umpire_counts.head())
