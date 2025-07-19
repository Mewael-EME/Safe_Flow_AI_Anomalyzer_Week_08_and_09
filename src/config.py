import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

FRAUD_DATA_PATH = os.path.join(RAW_DATA_DIR, "Fraud_Data.csv")
IP_TO_COUNTRY_PATH = os.path.join(RAW_DATA_DIR, "IpAddress_to_Country.csv")
