# Fraud Detection for E-commerce and Bank Transactions

## 🧠 Project Overview
This project aims to build robust ML models to detect fraudulent transactions in e-commerce and banking using transaction features, geolocation, and user behavior.

## 📁 Folder Structure
See folder breakdown above.

## 🛠️ How to Run
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python run_pipeline.py`
4. Explore the results in `reports/`

## 📊 Datasets Used
- `Fraud_Data.csv`
- `creditcard.csv`
- `IpAddress_to_Country.csv`

## 📌 Tasks Covered
- Data Cleaning & Feature Engineering
- Handling Imbalanced Classes
- Logistic Regression & Gradient Boosting Models
- Model Evaluation using AUC-PR, F1
- SHAP-based Explainability

## ✅ Features
- Cleans missing & duplicate values
- Merges geo-IP data
- Creates fraud-relevant features (hour, weekday, user frequency)
- Includes visuals and insights aligned to fraud behavior

## 💡 Usage
```bash
python /test_pipeline.py