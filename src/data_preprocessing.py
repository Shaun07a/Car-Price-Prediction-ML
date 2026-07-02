

import os
import pandas as pd


# -------------------------------
# File Paths
# -------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "raw",
    "car data.csv"
)

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "processed",
    "cleaned_car_data.csv"
)


# -------------------------------
# Load Dataset
# -------------------------------

def load_dataset(path):
    """
    Load the dataset.
    """
    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully.\n")
        return df

    except FileNotFoundError:
        print("Dataset not found!")
        return None


# -------------------------------
# Explore Dataset
# -------------------------------

def explore_dataset(df):

    print("=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)

    print("\nFirst Five Rows\n")
    print(df.head())

    print("\nDataset Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows :", df.duplicated().sum())


# -------------------------------
# Clean Dataset
# -------------------------------

def clean_dataset(df):

    print("\nRemoving duplicate rows...")

    df = df.drop_duplicates()

    print("Duplicates removed successfully.")

    return df


# -------------------------------
# Feature Engineering
# -------------------------------

def feature_engineering(df):

    CURRENT_YEAR = 2026

    df["Car_Age"] = CURRENT_YEAR - df["Year"]

    print("\nCar_Age feature created successfully.")

    return df


# -------------------------------
# Save Dataset
# -------------------------------

def save_dataset(df, path):

    df.to_csv(path, index=False)

    print("\nCleaned dataset saved successfully.")

    print(path)


# -------------------------------
# Main Function
# -------------------------------

def main():

    df = load_dataset(DATA_PATH)

    if df is None:
        return

    explore_dataset(df)

    df = clean_dataset(df)

    df = feature_engineering(df)

    save_dataset(df, OUTPUT_PATH)


if __name__ == "__main__":
    main()