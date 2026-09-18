# Customer Churn AI

## Customer Retention & Churn Risk Analytics

Customer Churn AI is a machine learning and business analytics project that predicts customer churn, identifies high-risk customers, and provides actionable retention insights.

The project combines customer analytics, machine learning, risk scoring, and an interactive Streamlit dashboard.

---

## Dashboard Preview

![Customer Churn AI Dashboard](outputs/churn_dashboard.png)

---

## Business Problem

Customer churn can significantly impact business revenue.

Businesses need to identify customers who are likely to leave so they can take proactive retention actions.

Customer Churn AI addresses this problem by:

* Predicting customer churn probability
* Identifying high-risk customers
* Highlighting valuable customers at risk
* Analyzing customer behavior
* Providing business-oriented retention insights

---

## Key Features

### Customer Analytics

* Customer demographics
* Customer tenure
* Monthly spending
* Total spending
* Number of orders
* Average order value
* Support interactions
* Days since last purchase
* Discount usage

### Churn Analysis

* Churn rate
* Active vs. churned customers
* Customer behavior comparison
* High-risk customer identification

### Machine Learning

* Random Forest classification
* Train/test split
* Feature scaling
* Churn probability prediction
* Classification report
* Customer risk classification

### Risk Segmentation

Customers are classified into:

* High Risk
* Medium Risk
* Low Risk

### Business Intelligence

The project identifies:

* High-value customers at risk
* Historical customer value associated with high-risk customers
* Customers with long periods since their last purchase
* Customers with frequent support interactions
* Potential retention priorities

---

## Machine Learning Results

The Random Forest model achieved:

* **Accuracy:** 83.0%

### Classification Report

| Customer Status | Precision | Recall | F1-Score |
| --------------- | --------: | -----: | -------: |
| Active          |      0.84 |   0.92 |     0.88 |
| Churned         |      0.81 |   0.64 |     0.72 |

The churn recall of **64%** means the model identified approximately 64% of the actual churned customers in the test set.

For a churn prediction system, recall for the churn class is an important metric because missing a customer who is likely to leave can reduce the opportunity for retention action.

---

## Business Insights Example

Using the sample dataset:

* **1,000 customers**
* **337 churned customers**
* **33.7% churn rate**
* **279 customers classified as high risk**
* Approximately **$3.52M historical total spending** associated with high-risk customers

> Note: The $3.52M figure represents the historical total spending of customers classified as high risk. It should not be interpreted as guaranteed future revenue loss.

High-risk customers showed longer periods since their last purchase, making recency an important factor in the churn analysis.

---

## Recommended Business Actions

1. Contact high-value customers with high churn probability.
2. Create personalized retention campaigns.
3. Follow up with customers who have not purchased recently.
4. Investigate customers with frequent support interactions.
5. Prioritize high-value customers for retention efforts.

---

## Project Workflow

```text
Customer Data
      ↓
Data Analysis
      ↓
Feature Preparation
      ↓
Machine Learning Model
      ↓
Churn Probability
      ↓
Risk Classification
      ↓
High-Risk Customer Analysis
      ↓
Business Insights
      ↓
Streamlit Dashboard
```

---

## Project Structure

```text
Customer Churn AI
│
├── data
│   └── customers.csv
│
├── models
│   ├── churn_model.pkl
│   └── scaler.pkl
│
├── outputs
│   ├── churn_dashboard.png
│   ├── churn_distribution.png
│   ├── last_purchase_by_churn.png
│   ├── support_calls_by_churn.png
│   └── high_risk_customers.csv
│
├── app
│   └── dashboard.py
│
├── create_data.py
├── churn_analysis.py
├── churn_charts.py
├── train_model.py
├── predict_churn.py
├── high_risk_customers.py
├── business_insights.py
├── requirements.txt
└── README.md
```

---

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Matplotlib
* Streamlit

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/DataNovaAI/Customer-Churn-AI.git
cd Customer-Churn-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit dashboard

```bash
streamlit run app/dashboard.py
```

---

## Dataset

The project currently uses a **synthetic customer dataset** containing 1,000 customers.

The dataset includes customer behavior and transaction-related features such as:

* Age
* Gender
* Tenure
* Monthly spending
* Total spending
* Number of orders
* Average order value
* Support calls
* Days since last purchase
* Discount usage
* Churn status

T
