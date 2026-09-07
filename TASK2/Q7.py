import pandas as pd


matches = pd.read_csv("matches.csv")

only_runs = matches[matches['win_by_runs'] > 0]

highest_value = only_runs['win_by_runs'].max()
lowest_value = only_runs['win_by_runs'].min()

highest_row = only_runs[only_runs['win_by_runs'] == highest_value]
lowest_row = only_runs[only_runs['win_by_runs'] == lowest_value]

print("Team which won by the highest number of runs:")
print(highest_row[['winner', 'win_by_runs']])

print("\nTeam which won by the lowest number of runs:")
print(lowest_row[['winner', 'win_by_runs']])
