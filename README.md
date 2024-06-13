# Telco Customer Churn Prediction

## Overview
This project is about developing a customer churn prediction service in the telecommunications context using various machine learning models.

## Folder Structure
- `api/`: Contains the Flask API for local model hosting.
- `data/`: Contains the dataset to be processed as csv.
- `input/`: Contains original dataset as Excel and the task given as PDF document.
- `models/`: Contains the saved models.
- `notebooks/`: Contains the Jupyter notebook for EDA and model training.
- `tests/`: Contains the tests for the API.

## Usage
Follow these steps to be able to replicate the analyses and test the model API service.


1. **Installation / Prerequisites.** Create a virtual environment and install the dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows (Git Bash): source venv/Scripts/activate
    pip install -r requirements.txt
    ```

2. **(Optional: Notebook)** Open `notebooks/churn_prediction.ipynb` in your local Jupyter Notebook and re-run the analysis to follow along the data analysis and model training. At the end of the model training, the best model (pipelines) among various different machine learning models (pipelines) is chosen and saved as serialized file. It can be replicated since a fixed random state (seed) is pre-selected (relevant for randomness of train-test splits and cross-validation during hyperparameter-tuning).

3. **Test Run with API.** Open two command-line terminal instances (sessions):
   1. Type `python api/run.py` to start the Flask API and provision it at localhost:5000
   2. Type `python tests/run.py` to send a test request to the API. There is a set of two arbitrary dummy customers with more or less plausible feature values in `data/test_data.json`. Feel free to modify the test file or add dummy customers to play around.