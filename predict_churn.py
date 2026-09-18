import pandas as pd
import joblib


# Load trained model and scaler
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# New customer
new_customer = pd.DataFrame({
    "Age": [35],
    "Tenure_Months": [12],
    "Monthly_Spend": [450],
    "Total_Spend": [5400],
    "Num_Orders": [10],
    "Avg_Order_Value": [540],
    "Support_Calls": [6],
    "Last_Purchase_Days": [140],
    "Discount_Usage": [2]
})


# Scale customer data
new_customer_scaled = scaler.transform(new_customer)


# Predict churn
prediction = model.predict(new_customer_scaled)

probability = model.predict_proba(
    new_customer_scaled
)[0][1]


# Display result
print("\n--- Customer Churn Prediction ---")

if prediction[0] == 1:
    print("Prediction: HIGH CHURN RISK")
else:
    print("Prediction: LOW CHURN RISK")

print(f"Churn Probability: {probability:.2%}")