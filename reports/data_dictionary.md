# Data Dictionary

## dim_fund

Source: 01_fund_master.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Asset management company |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| risk_category | TEXT | Risk classification |

---

## fact_nav

Source: clean_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

Source: clean_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Scheme identifier |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| kyc_status | TEXT | KYC verification status |

---

## fact_performance

Source: clean_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year return (%) |
| return_5yr_pct | REAL | 5-year return (%) |
| expense_ratio_pct | REAL | Fund expense ratio (%) |

---

## fact_aum

Source: 03_aum_by_fund_house.csv

| Column | Type | Description |
|----------|----------|----------|
| fund_house | TEXT | AMC name |
| aum_crore | REAL | Assets Under Management (₹ crore) |
| num_schemes | INTEGER | Number of schemes |
| date | DATE | Reporting date |