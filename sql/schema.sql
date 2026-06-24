CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    day INTEGER,
    month INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    txn_id INTEGER PRIMARY KEY,
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date DATE,
    transaction_type TEXT,
    amount_inr REAL
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_house TEXT,
    aum_crore REAL,
    num_schemes INTEGER,
    report_date DATE
);