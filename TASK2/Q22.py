import pandas as pd
import matplotlib.pyplot as plt


matches = pd.read_csv("matches.csv")


toss_win_count = matches['toss_winner'].value_counts()

toss_win_count.plot(kind='bar', figsize=(10, 6), color='orange')
plt.title("Toss Wins of All Teams")
plt.xlabel("Team")
plt.ylabel("Number of Toss Wins")
plt.tight_layout()
plt.savefig("Q22.png")
plt.show()
