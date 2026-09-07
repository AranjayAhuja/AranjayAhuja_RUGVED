import pandas as pd
import matplotlib.pyplot as plt


matches = pd.read_csv("matches.csv")

winner_distribution = matches['winner'].value_counts()

print("Distribution of match winners:")
print(winner_distribution)

winner_distribution.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title("Distribution of Teams Who Won Matches")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.tight_layout()
plt.savefig("Q21.png")
plt.show()
