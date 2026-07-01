import pandas as pd

performance = pd.read_csv(
    "data/processed/clean_scheme_performance.csv"
)

risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
).strip().title()

# Map user input to dataset values
risk_mapping = {
    "Low": ["Low"],
    "Moderate": ["Moderate", "Moderately High"],
    "High": ["High", "Very High"]
}

if risk not in risk_mapping:
    print("\nInvalid input! Please enter Low, Moderate, or High.")

else:
    filtered = performance[
        performance["risk_grade"].isin(risk_mapping[risk])
    ]

    recommendations = (
        filtered
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    print("\nTop 3 Recommended Funds\n")
    print(
        recommendations[
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct",
                "expense_ratio_pct"
            ]
        ].to_string(index=False)
    )