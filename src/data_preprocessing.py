import pandas as pd
from src.config import FRAUD_DATA_PATH, IP_TO_COUNTRY_PATH
from src.utils import convert_ip_to_int

def load_fraud_data():
    """Load raw fraud transaction data from configured path."""
    return pd.read_csv(FRAUD_DATA_PATH)

def clean_fraud_data(df):
    """Clean raw data: handle missing values, remove duplicates, convert types."""
    df = df.drop_duplicates()

    # Drop rows with critical missing values only
    df = df.dropna(subset=['purchase_value', 'ip_address'])

    # Convert transaction time
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

    # Convert IP to integer
    df["ip_integer"] = df["ip_address"].apply(convert_ip_to_int).astype("Int64")

    return df

def merge_with_geolocation(fraud_df):
    """Merge cleaned fraud data with geolocation info using IP ranges."""
    ip_df = pd.read_csv(IP_TO_COUNTRY_PATH)

    # Ensure IP bounds are integer typed
    ip_df["lower_bound_ip_address"] = ip_df["lower_bound_ip_address"].astype("Int64")
    ip_df["upper_bound_ip_address"] = ip_df["upper_bound_ip_address"].astype("Int64")

    # Perform range-based merge using asof and filtering upper bounds
    merged_df = pd.merge_asof(
        fraud_df.sort_values("ip_integer"),
        ip_df.sort_values("lower_bound_ip_address"),
        left_on="ip_integer",
        right_on="lower_bound_ip_address",
        direction="backward"
    )

    merged_df = merged_df[merged_df["ip_integer"] <= merged_df["upper_bound_ip_address"]]
    return merged_df
