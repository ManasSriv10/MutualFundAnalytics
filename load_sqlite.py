import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)


fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")

nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")


txn = pd.read_csv(
    "data/processed/clean_investor_transactions.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")


perf = pd.read_csv(
    "data/processed/clean_scheme_performance.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")


aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum loaded")

print("\nDatabase Loading Complete")