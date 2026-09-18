import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

num_customers = 1000

customer_ids = [
    f"Customer_{i:04d}"
    for i in range(1, num_customers + 1)
]

ages = np.random.randint(18, 70, num_customers)

genders = np.random.choice(
    ["Male", "Female"],
    size=num_customers
)

tenure = np.random.randint(1, 61, num_customers)

monthly_spend = np.round(
    np.random.uniform(20, 1000, num_customers),
    2
)

total_spend = np.round(
    monthly_spend * tenure,
    2
)

num_orders = np.maximum(
    1,
    np.round(
        tenure * np.random.uniform(
            0.5,
            2.5,
            num_customers
        )
    )
).astype(int)

avg_order_value = np.round(
    total_spend / num_orders,
    2
)

support_calls = np.random.poisson(
    2,
    num_customers
)

last_purchase_days = np.random.randint(
    1,
    181,
    num_customers
)

discount_usage = np.random.poisson(
    3,
    num_customers
)

churn_score = (
    0.035 * last_purchase_days
    + 0.8 * support_calls
    - 0.025 * num_orders
    - 0.03 * tenure
)

churn_probability = 1 / (
    1 + np.exp(-(
        churn_score - np.percentile(churn_score, 70)
    ))
)

churn = np.random.binomial(
    1,
    churn_probability
)

df = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Age": ages,
    "Gender": genders,
    "Tenure_Months": tenure,
    "Monthly_Spend": monthly_spend,
    "Total_Spend": total_spend,
    "Num_Orders": num_orders,
    "Avg_Order_Value": avg_order_value,
    "Support_Calls": support_calls,
    "Last_Purchase_Days": last_purchase_days,
    "Discount_Usage": discount_usage,
    "Churn": churn
})

df.to_csv(
    "data/customers.csv",
    index=False
)

print("Customer churn dataset created successfully!")
print(f"Number of customers: {len(df)}")
print(f"Churned customers: {df['Churn'].sum()}")