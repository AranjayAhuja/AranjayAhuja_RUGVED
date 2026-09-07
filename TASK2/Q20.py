import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


matches = pd.read_csv("matches.csv")

team1_count = matches['team1'].value_counts()
team2_count = matches['team2'].value_counts()
total_matches_team = team1_count.add(team2_count, fill_value=0)

win_count = matches['winner'].value_counts()

team_stats = pd.DataFrame({
    'total_matches': total_matches_team,
    'wins': win_count
})
team_stats = team_stats.fillna(0)
team_stats['win_rate'] = team_stats['wins'] / team_stats['total_matches']

fig, ax1 = plt.subplots(figsize=(12, 7))

x = np.arange(len(team_stats.index))
width = 0.35

ax1.bar(x - width/2, team_stats['total_matches'], width, label='Total Matches')
ax1.bar(x + width/2, team_stats['wins'], width, label='Winning Matches')
ax1.set_xticks(x)
ax1.set_xticklabels(team_stats.index, rotation=90)
ax1.set_ylabel("Number of Matches")
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(x, team_stats['win_rate'], color='black', marker='o', label='Win Rate')
ax2.set_ylabel("Win Rate")
ax2.legend(loc='upper right')

plt.title("Total Matches vs Winning Matches vs Win Rate")
plt.tight_layout()
plt.savefig("q20_matches_vs_wins_vs_winrate.png")
plt.show()
