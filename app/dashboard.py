import streamlit as st
import pandas as pd


# Page configuration
st.set_page_config(
    page_title="Customer Churn AI",
    page_icon="📊",
    layout="wide"
)


# Load data
df = pd.read_csv("data/customers.csv")
risk_df = pd.read_csv("outputs/high_risk_customers.csv")


# Title
st.title("Customer Churn AI")
st.subheader("Customer Retention & Churn Risk Dashboard")


# KPI calculations
total_customers = len(df)

churned_customers = df["Churn"].sum()

churn_rate = df["Churn"].mean() * 100

high_risk_customers = len(risk_df)

customer_value_at_risk = risk_df["Total_Spend"].sum()


# KPI cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Churned Customers",
    f"{churned_customers:,}"
)

col3.metric(
    "Churn Rate",
    f"{churn_rate:.1f}%"
)

col4.metric(
    "High-Risk Customers",
    f"{high_risk_customers:,}"
)

col5.metric(
    "Customer Value at Risk",
    f"${customer_value_at_risk:,.0f}"
)


st.divider()


# Churn distribution
st.header("Churn Distribution")

churn_chart = (
    df["Churn"]
    .value_counts()
    .rename({
        0: "Active",
        1: "Churned"
    })
)

st.bar_chart(churn_chart)


st.divider()


# High-risk customers
st.header("Top High-Risk Customers")

top_risk = risk_df.sort_values(
    "Churn_Probability",
    ascending=False
).head(10)

display_columns = [
    "Customer_ID",
    "Churn_Probability",
    "Risk_Level",
    "Monthly_Spend",
    "Total_Spend",
    "Support_Calls",
    "Last_Purchase_Days"
]

st.dataframe(
    top_risk[display_columns],
    use_container_width=True
)


st.divider()


# Business insights
st.header("Business Insights")

st.write(
    f"🔴 **{high_risk_customers} customers** "
    "are currently classified as high churn risk."
)

st.write(
    f"💰 Their historical total spending is approximately "
    f"**${customer_value_at_risk:,.0f}**."
)

st.write(
    "📅 High-risk customers have generally gone longer "
    "without making a purchase."
)

st.write(
    "🎯 High-value customers with high churn probability "
    "should receive priority retention campaigns."
)

st.write(
    "📞 Customers with frequent support interactions "
    "should be investigated for potential service issues."
)


st.divider()

st.caption(
    "Customer Churn AI — Machine Learning & Business Analytics"
)