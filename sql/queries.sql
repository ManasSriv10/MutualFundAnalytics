-- 1. Top 5 Fund Houses by AUM

SELECT
    fund_house,
    MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV by Fund

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Highest NAV Recorded

SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC
LIMIT 10;

-- 4. Transaction Count by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Transaction Volume by Type

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 7. Top 10 Funds by 1-Year Return

SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 8. Average Returns Across Funds

SELECT
    AVG(return_1yr_pct) AS avg_1yr,
    AVG(return_3yr_pct) AS avg_3yr,
    AVG(return_5yr_pct) AS avg_5yr
FROM fact_performance;

-- 9. Risk Grade Distribution

SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;

-- 10. Number of Schemes by Fund House

SELECT
    fund_house,
    COUNT(*) AS scheme_count
FROM dim_fund
GROUP BY fund_house
ORDER BY scheme_count DESC;