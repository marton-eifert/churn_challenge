"""
This is a simple flask API that takes a POST request with a JSON payload and returns a JSON response.
The API is provided at port 5000 and the endpoint is /predict_churn.
"""

import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify


app = Flask(__name__)


def process(data):

    # Drop customerID
    data = data.drop(columns=['customerID'])

    # Transform to binary value range {0, 1}
    binary_features = [
        'gender',
        'Partner',
        'Dependents',
        'PhoneService',
        'PaperlessBilling',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'MultipleLines'
    ]
    data[binary_features] = data[binary_features].map(lambda x: 1 if (x == 'Yes' or x == 'Female') else 0)
    # Map: 0 (Month-to-month), 0.5 (One year), 1.0 (Two year): Standardization to range 0 to 1.0 with equal distance
    data['Contract'] = data['Contract'].map(lambda x: 1.0 if x == 'Two year' else 0.5 if x == 'One year' else 0)

    # Map: 0 (No Internet Service), 0.75 (DSL), 1.0 (Fiber optic): Standardization to range 0 to 1.0 with less distance between DSL and Fiber optic as they both are internet services
    data['InternetService'] = data['InternetService'].map(lambda x: 1.0 if x == 'Fiber optic' else 0.75 if x == 'DSL' else 0)

    # Scale the integer columns by dividing by 24 (which is the number of months in 2 years)
    data['tenure'] = data['tenure'] / 24

    return data



# Define the `predict_churn` endpoint
@app.route('/predict_churn', methods=['POST'])
def predict_churn():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Transform the data to a format that the model can use
    
    # Convert the JSON data to a pandas DataFrame
    data_df = pd.DataFrame(data, index=range(len(data)), columns=data[0].keys())
    print("DataFrame info before processing:")
    print(data_df.info())

    # Process the data
    data_df = process(data_df)
    print("DataFrame info after processing:")
    print(data_df.info())

    # Make a prediction using the model: predict and predict_proba
    prediction = model.predict(data_df)
    prediction_proba = model.predict_proba(data_df)[:, 1]

    print(prediction)
    print(prediction_proba)

    # # Return the prediction as a JSON response
    return jsonify({
        'prediction': prediction.tolist(),
        'prediction_proba': prediction_proba.tolist()
    })

if __name__ == '__main__':

    # Load the model on startup from the latest file in the ../models directory
    file_path = os.path.abspath(os.path.join(os.getcwd(), 'models'))
    print(file_path)
    latest_model = max([f for f in os.listdir(file_path) if f.endswith('.pkl')])
    model = joblib.load(os.path.join(file_path, latest_model))
    print(f'Loaded model {latest_model}')

    # Run the API
    app.run(port=5000, debug=True)