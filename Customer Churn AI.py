import pandas as pd
import joblib


# Load data
df = pd.read_csv("data/customers.csv")


# Load model and scaler
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# Features used by the model
features = [
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


# Prepare customer data
X = df[features]

X_scaled = scaler.transform(X)


# Predict churn probability
churn_probability = model.predict_proba(X_scaled)[:, 1]

df["Churn_Probability"] = churn_probability


# Create risk level
def risk_level(probability):

    if probability >= 0.70:
        return "High Risk"

    elif probability >= 0.40:
        return "Medium Risk"

    else:
        return "Low Risk"


df["Risk_Level"] = df["Churn_Probability"].apply(risk_level)


# Select high-risk customers
high_risk = df[
    df["Risk_Level"] == "High Risk"
].sort_values(
    "Churn_Probability",
    ascending=False
)


# Save results
high_risk.to_csv(
    "outputs/high_risk_customers.csv",
    index=False
)


# Display results
print("\n--- Churn Risk Analysis ---")

print(f"Total customers: {len(df)}")
print(f"High-risk customers: {(df['Risk_Level'] == 'High Risk').sum()}")
print(f"Medium-risk customers: {(df['Risk_Level'] == 'Medium Risk').sum()}")
print(f"Low-risk customers: {(df['Risk_Level'] == 'Low Risk').sum()}")


print("\n--- Top 10 High-Risk Customers ---")

print(
    high_risk[
        [
            "Customer_ID",
            "Churn_Probability",
            "Risk_Level",
            "Monthly_Spend",
            "Total_Spend",
            "Support_Calls",
            "Last_Purchase_Days"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


print("\nHigh-risk customer report saved successfully!")