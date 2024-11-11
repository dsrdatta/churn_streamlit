# utils/data_processing.py

import pandas as pd
import numpy as np
from config import DATA_PATH

def load_and_preprocess_data():
    """Loads and preprocesses data, including handling NaNs and encoding."""
    data = pd.read_csv(DATA_PATH)
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data['SeniorCitizen'] = data['SeniorCitizen'].astype(object)

    # Define categorical and numerical features
    cat_features = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
        'Contract', 'PaperlessBilling', 'PaymentMethod'
    ]
    num_features = ['tenure', 'MonthlyCharges', 'TotalCharges']

    # Set the target variable
    data['Churn'] = data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    # Process categorical and numerical features
    X_cat = pd.get_dummies(data[cat_features], drop_first=True)
    X_num = data[num_features].copy()
    X_num['TotalCharges'] = X_num['TotalCharges'].fillna(X_num['tenure'] * X_num['MonthlyCharges'])
    
    # Combine processed features
    X = pd.concat([X_cat, X_num], axis=1)
    return data, X


def get_data():
    """Wrapper function to load and preprocess data."""
    data, X = load_and_preprocess_data()
    return data  # Return the original data for filtering and display purposes

def filter_data(data, gender=None, internet_service=None, contract=None):
    """Filters the data based on sidebar selections."""
    filtered_data = data.copy()
    if gender:
        filtered_data = filtered_data[filtered_data['gender'].isin(gender)]
    if internet_service:
        filtered_data = filtered_data[filtered_data['InternetService'].isin(internet_service)]
    if contract:
        filtered_data = filtered_data[filtered_data['Contract'].isin(contract)]
    return filtered_data