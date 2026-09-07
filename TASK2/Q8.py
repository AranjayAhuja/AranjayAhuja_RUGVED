import pandas as pd
import numpy as np


matches = pd.read_csv("matches.csv")


mean_runs = np.mean(matches['win_by_runs'])
median_runs = np.median(matches['win_by_runs'])
std_runs = np.std(matches['win_by_runs'])

print("Mean of win_by_runs =", mean_runs)
print("Median of win_by_runs =", median_runs)
print("Standard Deviation of win_by_runs =", std_runs)
