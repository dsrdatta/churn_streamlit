# 📊 Customer Churn Prediction App

![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-red?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-Data%20Science-yellow?style=for-the-badge&logo=python)

## 🌟 Overview

The **Customer Churn Prediction App** is a Streamlit-based data analytics and prediction tool designed to analyze customer churn patterns in telecom data. This app uses a pre-trained logistic regression model to predict customer churn probability and provides insights into various customer attributes, helping stakeholders identify factors that influence customer retention.

## 🚀 Features

- **Interactive Filtering:** Easily filter customer data by gender, internet service type, and contract type.
- **Customer Insights:** View churn rate, average monthly charges, and customer segmentation based on various attributes.
- **Data Visualization:** Detailed charts to help understand trends and patterns in customer behavior.
- **Churn Prediction:** Predict the probability of churn for individual customers using a logistic regression model.

## 📂 Project Structure

```plaintext
project/
├── app.py                    # Main Streamlit app
├── config.py                 # Configuration file for paths and constants
├── requirements.txt          # Dependencies for the project
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Raw CSV file
│   └── processed_data.pkl    # Cached processed data (optional)
├── model/
│   └── model_logistic_v1.pkl # Trained model file
└── utils/
    ├── __init__.py
    ├── data_processing.py    # Functions for loading and preprocessing data
    └── prediction.py         # Functions to load the model and make predictions
