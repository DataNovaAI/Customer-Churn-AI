import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
df = pd.read_csv("data/customers.csv")


# Select features
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

X = df[features]
y = df["Churn"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Scale features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Create model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)


# Train model
model.fit(X_train_scaled, y_train)


# Make predictions
y_pred = model.predict(X_test_scaled)


# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\n--- Model Results ---")
print(f"Accuracy: {accuracy:.4f}")

print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))


# Save model and scaler
joblib.dump(model, "models/churn_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\nModel saved successfully!")