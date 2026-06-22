import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_in_nav = master_codes - nav_codes
missing_in_master = nav_codes - master_codes

print("Total AMFI Codes in Fund Master:", len(master_codes))
print("Total AMFI Codes in NAV History:", len(nav_codes))

print("\nCodes present in Fund Master but missing in NAV History:")
print(len(missing_in_nav))

print("\nCodes present in NAV History but missing in Fund Master:")
print(len(missing_in_master))