from src.data_preprocessing import load_fraud_data, clean_fraud_data, merge_with_geolocation
from src.feature_engineering import create_time_features, calculate_transaction_frequency
import pandas as pd

def test_pipeline():
    df = load_fraud_data()
    print("[Step 1] Raw fraud data shape:", df.shape)

    df_cleaned = clean_fraud_data(df)
    print("[Step 2] Cleaned data shape:", df_cleaned.shape)

    df_merged = merge_with_geolocation(df_cleaned)
    print("[Step 3] Merged with IP ranges:", df_merged.shape)

    df_feat = create_time_features(df_merged)
    df_feat = calculate_transaction_frequency(df_feat)

    print("[Step 4] Final processed data preview:")
    print(df_feat.head())

    df_feat.to_csv("data/processed/cleaned_fraud_data.csv", index=False)

if __name__ == "__main__":
    test_pipeline()
