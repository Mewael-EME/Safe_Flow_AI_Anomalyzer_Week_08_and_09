# Fraud Detection for E-commerce and Bank Transactions

## 🧠 Project Overview
This project aims to build robust ML models to detect fraudulent transactions in e-commerce and banking using transaction features, geolocation, and user behavior.

## 📁 Folder Structure
```
├── data/
│ ├── raw/ # Original datasets
│ ├── interim/ # Cleaned datasets
│ └── processed/ # Engineered feature sets
├── notebooks/
│ ├── Task1_Data_Engineering.ipynb
│ ├── Task2_Model_Building.ipynb
│ └── Task3_Model_Explainability_SHAP.ipynb
├── models/ # Trained model files
├── reports/ # Plots, metrics, SHAP explanations
├── src/ # Source code (data loader, model, utils)
├── test_pipeline.py # Pipeline test script
├── run_pipeline.py # Main pipeline script
├── requirements.txt
└── README.md ``` 


## 🛠️ How to Run
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python run_pipeline.py`
4. Explore the results in `notebooks/`

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
## 📈 Reports & Visuals
- Performance Metrics: AUC, Precision-Recall, F1
- Plots:
    - ROC Curve
    - Precision-Recall Curve
    - Confusion Matrix
    - SHAP Summary Plot

- Find these in reports/ or explore interactively in:
    - notebooks/Task2_Model_Building.ipynb
    - notebooks/Task3_Model_Explainability_SHAP.ipynb

## 💡 Usage
```bash
To run the pipeline:
python run_pipeline.py

To run the pipeline test:
python test_pipeline.py

To visualize model explainability:
Open notebooks/Task3_Model_Explainability_SHAP.ipynb
