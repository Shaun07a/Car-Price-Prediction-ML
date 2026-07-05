# Car Price Prediction using Machine Learning

An end-to-end Machine Learning web application that predicts the resale price of a used car based on its specifications. The application is built using **Python, Flask, Scikit-learn**, and deployed on **Render** with an interactive web interface.

---

## Live Demo

**Render Deployment:**  
https://car-price-prediction-ml-nmx9.onrender.com



---

## Project Overview

This project uses a trained **Random Forest Regression** model to estimate the selling price of a used car based on several vehicle attributes.

Users can enter details such as:

- Present Price
- Kilometers Driven
- Car Age
- Number of Previous Owners
- Fuel Type
- Seller Type
- Transmission Type

The trained model processes these inputs and instantly predicts the estimated resale value.

---

## Features

- End-to-end Machine Learning pipeline
- Data preprocessing and feature engineering
- Random Forest Regression model
- Interactive Flask web application
- Responsive Bootstrap-based user interface
- Input validation
- Model serialization using Joblib
- Cloud deployment using Render
- GitHub version control

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Exploratory Data Analysis
5. Model Training
6. Model Evaluation
7. Model Serialization
8. Flask Integration
9. Web Deployment

---

## Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Backend

- Flask
- Gunicorn

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Deployment

- Render

### Version Control

- Git
- GitHub

---

## Project Structure

```
Car-Price-Prediction-ML
│
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
├── .gitignore
│
├── dataset
│   ├── raw
│   └── processed
│
├── model
│   └── saved_models
│       └── car_price_pipeline.pkl
│
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── predictor.py
│
├── static
│   ├── css
│   ├── images
│   └── js
│
└── templates
    └── index.html
```

---

## Dataset

This project uses the **Car Details Dataset** containing historical used car listings and vehicle specifications.

Features include:

- Car Name
- Year
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner

Target Variable:

- Selling Price

---

## Model Used

**Random Forest Regressor**

The model was selected due to its strong performance on tabular regression problems and its ability to capture non-linear relationships between vehicle attributes and selling price.

---

## Running Locally

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Car-Price-Prediction-ML.git
```

Navigate to the project

```bash
cd Car-Price-Prediction-ML
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Support for additional regression models
- Confidence interval estimation
- Model comparison dashboard
- Vehicle image upload
- Historical prediction logging
- User authentication
- REST API integration

---



## Author

**Shaun Joseph**


## License

This project is developed for educational purposes and portfolio demonstration.
