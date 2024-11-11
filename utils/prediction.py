# utils/prediction.py

import pickle
import streamlit as st
from config import MODEL_PATH
from utils.data_processing import load_and_preprocess_data

@st.cache_resource
def load_model():
    """Loads the logistic model, caching it in memory."""
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def predict_churn(customerID, model):
    """Fetches preprocessed data for a customer and makes churn prediction."""
    data, X = load_and_preprocess_data()

    # Select data for the specified customer ID or a random sample
    if not customerID or sum(data['customerID'] == customerID) == 0:
        #X = X.sample(1)
        raise KeyError("Missing columns in the dataset")
    else:
        X = X[data['customerID'] == customerID]

    y_pred = model.predict(X)
    y_proba = model.predict_proba(X)
    return y_pred[0], y_proba[0, 1]
