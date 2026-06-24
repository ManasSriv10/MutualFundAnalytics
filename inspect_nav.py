import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)