# Data Quality Summary

## Dataset Overview

Datasets Checked:
- Fund Master
- NAV History
- AUM Data
- SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

## Fund Master

Key Fields:
- amfi_code
- fund_house
- scheme_name
- category
- sub_category
- risk_category

Checks:
- Missing values checked
- Duplicate rows checked

## NAV History

Key Fields:
- amfi_code
- nav
- date

Checks:
- Missing values checked
- Duplicate rows checked

## AMFI Validation

Result:
All AMFI codes in fund_master were compared with nav_history.

Status:
PASS

No AMFI code mismatches detected.

## Investor Transactions

Checks Performed:

- Transaction date converted to datetime

- Transaction type standardized

- Amount validation (amount_inr > 0)

- Duplicate records removed

- KYC status validated

Valid KYC Values:
- Verified
- Pending

Invalid KYC Records:
0

## Scheme Performance

Checks Performed:

- Return columns converted to numeric

- Missing return values checked

- Expense ratio validated

Valid Range:
0.1% – 2.5%

Anomaly Count:
0