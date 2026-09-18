import pandas as pd


# Load high-risk customers
df = pd.read_csv(
    "outputs/high_risk_customers.csv"
)


# Basic statistics
total_high_risk = len(df)

total_revenue_at_risk = df["Total_Spend"].sum()

average_monthly_spend = df["Monthly_Spend"].mean()

average_last_purchase = df["Last_Purchase_Days"].mean()

average_support_calls = df["Support_Calls"].mean()


# Display insights
print("\n--- Customer Churn Business Insights ---")

print(
    f"High-risk customers: {total_high_risk}"
)

print(
    f"Total customer value at risk: "
    f"${total_revenue_at_risk:,.2f}"
)

print(
    f"Average monthly spend of high-risk customers: "
    f"${average_monthly_spend:,.2f}"
)

print(
    f"Average days since last purchase: "
    f"{average_last_purchase:.1f} days"
)

print(
    f"Average support calls: "
    f"{average_support_calls:.1f}"
)


# Top valuable customers at risk
top_value_at_risk = df.sort_values(
    "Total_Spend",
    ascending=False
).head(10)


print("\n--- Top Valuable Customers at Risk ---")

print(
    top_value_at_risk[
        [
            "Customer_ID",
            "Total_Spend",
            "Churn_Probability",
            "Last_Purchase_Days"
        ]
    ].to_string(index=False)
)


print("\n--- Recommended Actions ---")

print("1. Contact high-value customers with high churn probability.")

print("2. Offer personalized retention discounts.")

print("3. Follow up with customers who have not purchased recently.")

print("4. Investigate customers with frequent support calls.")

print("5. Prioritize customers with high total spending.")