import pandas as pd

matches = pd.read_csv("matches.csv")

city_counts = matches['city'].value_counts()

max_city = city_counts.idxmax()
max_value = city_counts.max()

min_city = city_counts.idxmin()
min_value = city_counts.min()

print("City with maximum matches =", max_city, "with", max_value, "matches")
print("City with minimum matches =", min_city, "with", min_value, "matches")
