import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print(df.head())

print(df.columns.tolist())

print(df.dtypes)