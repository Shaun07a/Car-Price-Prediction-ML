

import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset Paths
RAW_DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "raw",
    "car data.csv"
)

PROCESSED_DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "processed",
    "cleaned_car_data.csv"
)

# Model Path
MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "saved_models",
    "car_price_pipeline.pkl"
)