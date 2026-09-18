import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/customers.csv")

# Create outputs folder
os.makedirs("outputs", exist_ok=True)


# 1. Churn Distribution
churn_counts = df["Churn"].value_counts()

plt.figure(figsize=(6, 5))

plt.bar(
    ["Active", "Churned"],
    [
        churn_counts.get(0, 0),
        churn_counts.get(1, 0)
    ]
)

plt.title("Customer Churn Distribution")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("outputs/churn_distribution.png")

plt.close()


# 2. Last Purchase Days by Churn
avg_last_purchase = df.groupby("Churn")["Last_Purchase_Days"].mean()

plt.figure(figsize=(6, 5))

plt.bar(
    ["Active", "Churned"],
    [
        avg_last_purchase.get(0, 0),
        avg_last_purchase.get(1, 0)
    ]
)

plt.title("Average Days Since Last Purchase")
plt.ylabel("Days")

plt.tight_layout()

plt.savefig("outputs/last_purchase_by_churn.png")

plt.close()


# 3. Support Calls by Churn
avg_support_calls = df.groupby("Churn")["Support_Calls"].mean()

plt.figure(figsize=(6, 5))

plt.bar(
    ["Active", "Churned"],
    [
        avg_support_calls.get(0, 0),
        avg_support_calls.get(1, 0)
    ]
)

plt.title("Average Support Calls by Churn Status")
plt.ylabel("Average Support Calls")

plt.tight_layout()

plt.savefig("outputs/support_calls_by_churn.png")

plt.close()


print("Churn charts created successfully!")