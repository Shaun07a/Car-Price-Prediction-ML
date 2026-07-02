

import os
import joblib
import pandas as pd

import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "processed",
    "cleaned_car_data.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "saved_models",
    "car_price_pipeline.pkl"
)

def load_dataset():

    df = pd.read_csv(DATA_PATH)

    print("Dataset Loaded Successfully\n")

    return df

def prepare_data(df):
    """
    Prepare feature matrix (X) and target variable (y).
    """

    # Create a copy
    df = df.copy()

    # Drop unnecessary columns
    df.drop(columns=["Car_Name", "Year"], inplace=True)

    # Features
    X = df.drop(columns=["Selling_Price"])

    # Target
    y = df["Selling_Price"]

    print("Data prepared successfully.\n")

    return X, y

def split_dataset(X, y):
    """
    Split the dataset into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    print("Dataset split successfully.\n")

    return X_train, X_test, y_train, y_test

def create_preprocessor():
    """
    Create preprocessing pipeline.
    """

    categorical_features = [
        "Fuel_Type",
        "Seller_Type",
        "Transmission"
    ]

    numeric_features = [
        "Present_Price",
        "Kms_Driven",
        "Owner",
        "Car_Age"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            ),
            (
                "numeric",
                "passthrough",
                numeric_features
            )
        ]
    )

    print("Preprocessor created successfully.\n")

    return preprocessor

def train_linear_regression(preprocessor, X_train, y_train):
    """
    Train a Linear Regression model using a pipeline.
    """

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", LinearRegression())
        ]
    )

    pipeline.fit(X_train, y_train)

    print("Linear Regression trained successfully.\n")

    return pipeline

def train_random_forest(preprocessor, X_train, y_train):
    """
    Train a Random Forest Regressor using a pipeline.
    """

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "model",
                RandomForestRegressor(
                    n_estimators=100,
                    random_state=42
                )
            )
        ]
    )

    pipeline.fit(X_train, y_train)

    print("Random Forest trained successfully.\n")

    return pipeline

def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model.
    """

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, predictions)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2 Score": r2
    }

def save_model(model):
    """
    Save the trained pipeline.
    """

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print("Model saved successfully.\n")
    print(MODEL_PATH)


def main():

    # Load Dataset
    df = load_dataset()

    # Prepare Data
    X, y = prepare_data(df)

    # Split Dataset
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Preprocessor
    preprocessor = create_preprocessor()

    # Train Models
    linear_model = train_linear_regression(
        preprocessor,
        X_train,
        y_train
    )

    random_forest_model = train_random_forest(
        preprocessor,
        X_train,
        y_train
    )

    # Evaluate Models
    linear_results = evaluate_model(
        linear_model,
        X_test,
        y_test
    )

    random_results = evaluate_model(
        random_forest_model,
        X_test,
        y_test
    )

    print("=" * 50)
    print("LINEAR REGRESSION")
    print("=" * 50)

    for key, value in linear_results.items():
        print(f"{key}: {value:.4f}")

    print()

    print("=" * 50)
    print("RANDOM FOREST")
    print("=" * 50)

    for key, value in random_results.items():
        print(f"{key}: {value:.4f}")

    # Select Best Model
    if random_results["R2 Score"] > linear_results["R2 Score"]:
        best_model = random_forest_model
        print("\nBest Model: Random Forest")
    else:
        best_model = linear_model
        print("\nBest Model: Linear Regression")

    # Save Best Model
    save_model(best_model)


if __name__ == "__main__":
    main()

