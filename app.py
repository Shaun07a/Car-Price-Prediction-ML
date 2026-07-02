from flask import Flask, render_template, request

from src.predictor import CarPricePredictor

app = Flask(__name__)

predictor = CarPricePredictor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    present_price = float(request.form["present_price"])
    kms_driven = int(request.form["kms_driven"])
    owner = int(request.form["owner"])
    fuel_type = request.form["fuel_type"]
    seller_type = request.form["seller_type"]
    transmission = request.form["transmission"]
    car_age = int(request.form["car_age"])

    prediction = predictor.predict(
        present_price,
        kms_driven,
        owner,
        fuel_type,
        seller_type,
        transmission,
        car_age
    )

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)