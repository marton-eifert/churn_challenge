"""
This is a simple test that sends a POST request a running API at port 5000 and checks the response.
"""
import requests
import json
import os


if __name__ == '__main__':

    file_path = os.path.abspath(os.path.join(os.getcwd(), 'data'))
    print(file_path)
    
    # Load the test data
    with open(os.path.join(file_path, 'test_data.json'), 'r') as f:
        test_data = json.load(f)

    print(test_data)

    # Send a POST request to the API
    response = requests.post('http://localhost:5000/predict_churn', json=test_data)
    print(response)

    # Check the response
    response_data = response.json()
    print(response_data)
    assert 'prediction' in response_data
    assert 'prediction_proba' in response_data
    assert len(response_data['prediction']) == len(test_data)
    assert len(response_data['prediction_proba']) == len(test_data)

    # prediction should be either 0 or 1
    assert response_data['prediction'][0] in [0, 1]
    # prediction_proba should be any float between 0.0 and 1.0
    assert 0.0 <= response_data['prediction_proba'][0] <= 1.0
    
    print('Test passed!')