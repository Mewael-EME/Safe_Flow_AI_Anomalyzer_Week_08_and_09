# src/data_transformation.py

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

def encode_and_scale(df, categorical_cols, numerical_cols):
    df = df.copy()

    # One-hot encode categorical
    df = pd.get_dummies(df, columns=categorical_cols)

    # Scale numeric features
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df

def handle_class_imbalance(X, y, method='smote'):
    if method == 'smote':
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X, y)
        return X_resampled, y_resampled
    else:
        raise NotImplementedError("Only SMOTE is implemented.")
