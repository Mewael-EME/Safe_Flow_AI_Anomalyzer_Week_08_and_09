from src.data_preprocessing import load_fraud_data, clean_fraud_data, merge_with_geolocation
from src.feature_engineering import create_time_features, calculate_transaction_frequency
import pandas as pd

def run():
    print("[Step 1] Loading raw fraud data...")
    df = load_fraud_data()
    print(f"→ Raw shape: {df.shape}")

    print("[Step 2] Cleaning data...")
    df = clean_fraud_data(df)
    print(f"→ Cleaned shape: {df.shape}")

    print("[Step 3] Merging with geolocation data...")
    df = merge_with_geolocation(df)
    print(f"→ Merged shape: {df.shape}")

    print("[Step 4] Creating time-based features...")
    df = create_time_features(df)

    print("[Step 5] Calculating transaction frequency...")
    df = calculate_transaction_frequency(df)

    print("[Step 6] Saving cleaned and enriched data...")
    df.to_csv("data/processed/cleaned_fraud_data.csv", index=False)
    print("✅ Data pipeline executed successfully. Output saved at 'data/processed/cleaned_fraud_data.csv'.")

if __name__ == "__main__":
    run()
