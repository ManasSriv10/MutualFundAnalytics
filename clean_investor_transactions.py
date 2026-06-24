import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:")
print(df.shape)


df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)


df["transaction_type"] = (
    df["transaction_type"]
      .astype(str)
      .str.strip()
      .str.upper()
)

mapping = {
    "SIP": "SIP",
    "SYSTEMATIC INVESTMENT": "SIP",

    "LUMPSUM": "Lumpsum",
    "LUMP SUM": "Lumpsum",

    "REDEMPTION": "Redemption",
    "REDEEM": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
      .replace(mapping)
)


df = df[
    df["amount_inr"] > 0
]


print("\nUnique KYC Status Values:")

print(
    df["kyc_status"].unique()
)


df = df.drop_duplicates()

print("\nCleaned Shape:")
print(df.shape)


df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print(
    "\nclean_investor_transactions.csv saved"
)