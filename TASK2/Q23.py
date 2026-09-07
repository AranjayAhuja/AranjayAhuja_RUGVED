import pandas as pd
import matplotlib.pyplot as plt


matches = pd.read_csv("matches.csv")


top_5_teams = matches['winner'].value_counts().head(5)

top_5_teams.plot(kind='bar', figsize=(8, 6), color='green')
plt.title("Top 5 Teams with Most Wins")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.tight_layout()
plt.savefig("Q23.png")
plt.show()
