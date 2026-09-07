import pandas as pd


matches = pd.read_csv("matches.csv")

result_count = matches['result'].value_counts()

print("Result wise match count:")
print(result_count)
