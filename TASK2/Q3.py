import pandas as pd

matches = pd.read_csv("matches.csv")

citywise_count = matches['city'].value_counts()

print("Total count of matches city-wise:")
print(citywise_count)
