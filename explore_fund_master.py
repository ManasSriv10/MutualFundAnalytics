import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\n===== UNIQUE FUND HOUSES =====")
print(df["fund_house"].unique())
print("Count:", df["fund_house"].nunique())

print("\n===== UNIQUE CATEGORIES =====")
print(df["category"].unique())
print("Count:", df["category"].nunique())

print("\n===== UNIQUE SUB-CATEGORIES =====")
print(df["sub_category"].unique())
print("Count:", df["sub_category"].nunique())

print("\n===== UNIQUE RISK CATEGORIES =====")
print(df["risk_category"].unique())
print("Count:", df["risk_category"].nunique())

print("\n===== SAMPLE AMFI CODES =====")
print(df["amfi_code"].head(20))