import pandas as pd

# Load dataset
df = pd.read_csv("data/customers.csv")

# Basic information
print("\n--- Dataset Information ---")
print(f"Number of customers: {len(df)}")
print(f"Number of features: {df.shape[1]}")
print(f"Missing values: {df.isnull().sum().sum()}")

# Churn distribution
print("\n--- Churn Distribution ---")

churn_counts = df["Churn"].value_counts()

print(f"Active customers: {churn_counts.get(0, 0)}")
print(f"Churned customers: {churn_counts.get(1, 0)}")

churn_rate = df["Churn"].mean() * 100

print(f"Churn rate: {churn_rate:.2f}%")

# Average values by churn status
print("\n--- Customer Comparison ---")

comparison = df.groupby("Churn")[
    [
        "Age",
        "Tenure_Months",
        "Monthly_Spend",
        "Total_Spend",
        "Num_Orders",
        "Avg_Order_Value",
        "Support_Calls",
        "Last_Purchase_Days",
        "Discount_Usage"
    ]
].mean()

print(comparison)

# High-risk customers
print("\n--- High Risk Customers ---")

high_risk = df[
    (df["Last_Purchase_Days"] > 120) &
    (df["Support_Calls"] >= 4)
]

print(f"High-risk customers: {len(high_risk)}")

# Top customers by total spend
print("\n--- Top 10 Customers by Total Spend ---")

top_customers = df.nlargest(
    10,
    "Total_Spend"
)[
    [
        "Customer_ID",
        "Total_Spend",
        "Num_Orders",
        "Tenure_Months",
        "Churn"
    ]
]

print(top_customers.to_string(index=False))