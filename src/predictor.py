

import joblib
import pandas as pd

from src.config import MODEL_PATH


class CarPricePredictor:
    """
    Loads the trained pipeline and predicts car prices.
    """

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(
        self,
        present_price,
        kms_driven,
        owner,
        fuel_type,
        seller_type,
        transmission,
        car_age
    ):

        input_data = pd.DataFrame({
            "Present_Price": [present_price],
            "Kms_Driven": [kms_driven],
            "Fuel_Type": [fuel_type],
            "Seller_Type": [seller_type],
            "Transmission": [transmission],
            "Owner": [owner],
            "Car_Age": [car_age]
        })

        prediction = self.model.predict(input_data)

        return round(prediction[0], 2)