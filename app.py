from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Start with all 105 features set to 0
    input_df = pd.DataFrame([{col: 0 for col in columns}])

    # Fill numeric fields
    input_df['Year'] = int(request.form['year'])
    input_df['Present_Price'] = float(request.form['present_price'])
    input_df['Driven_kms'] = int(request.form['driven_kms'])
    input_df['Owner'] = int(request.form['owner'])

    # One-hot encode Fuel Type
    fuel = request.form['fuel_type']
    if fuel == 'Diesel' and 'Fuel_Type_Diesel' in columns:
        input_df['Fuel_Type_Diesel'] = 1
    elif fuel == 'Petrol' and 'Fuel_Type_Petrol' in columns:
        input_df['Fuel_Type_Petrol'] = 1

    # One-hot encode Selling Type
    if request.form['selling_type'] == 'Individual' and 'Selling_type_Individual' in columns:
        input_df['Selling_type_Individual'] = 1

    # One-hot encode Transmission
    if request.form['transmission'] == 'Manual' and 'Transmission_Manual' in columns:
        input_df['Transmission_Manual'] = 1

    # One-hot encode Car Name
    car_col = f"Car_Name_{request.form['car_name']}"
    if car_col in columns:
        input_df[car_col] = 1

    prediction = round(float(model.predict(input_df)[0]), 2)
    return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)