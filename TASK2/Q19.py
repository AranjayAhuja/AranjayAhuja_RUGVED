import pandas as pd
import matplotlib.pyplot as plt


matches = pd.read_csv("matches.csv")


toss_season = matches.groupby(['season', 'toss_decision']).size().unstack()

toss_season.plot(kind='bar', figsize=(10, 6))
plt.title("Toss Decisions Across All Seasons")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.legend(title="Toss Decision")
plt.tight_layout()
plt.savefig("Q19.png")
plt.show()
