import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:")
print(df.shape)


return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)


print("\nMissing Return Values:")

print(
    df[return_cols].isnull().sum()
)


anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "\nExpense Ratio Anomalies:"
)

print(
    len(anomalies)
)

df = df.drop_duplicates()

print("\nCleaned Shape:")
print(df.shape)

df.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print(
    "\nSaved clean_scheme_performance.csv"
)