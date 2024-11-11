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
```

## 📦 Installation

Clone the Repository

    git clone https://github.com/your-username/customer-churn-prediction-app.git
    cd customer-churn-prediction-app
    Install Dependencies
    pip install -r requirements.txt
    Run the Streamlit App
    streamlit run app.py

## 🔧 Configuration

Update config.py with the paths to your data and model files. Ensure the following variables point to the correct files:

# config.py
    DATA_PATH = 'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    MODEL_PATH = 'model/model_logistic_v1.pkl'

## 🧩 Usage

Filter Customer Data: Use the sidebar to filter customers by attributes like gender, contract type, and internet service.
View Metrics and Visualizations: Explore metrics like churn rate and average monthly charges, and view various customer insights through charts.
Predict Churn Probability: Select a customer ID to predict the churn probability and view the associated churn prediction.

## 📝 Sample Code Snippet

# Example: Loading and Preprocessing Data
    from utils.data_processing import get_data, filter_data
    from utils.prediction import load_model, predict_churn

# Load data and model
    data = get_data()
    model = load_model()

# Filter data and predict churn for a customer
    filtered_data = filter_data(data, gender=['Male'], contract=['Month-to-month'])
    y_pred, y_proba = predict_churn(customer_id='12345', model=model)

## 🧩 Modules

    app.py: The main application script, managing the Streamlit interface and layout.
    config.py: Stores file paths and configuration settings.
    utils/data_processing.py: Contains functions to load, preprocess, and filter data.
    utils/prediction.py: Loads the model and defines the churn prediction function.

## 📊 Visualizations

This app includes various visualizations, such as:

- Churn Rate by Payment Method
- Total Charges by Contract Type
- Average Monthly Charges by Gender & Senior Citizen Status
- Overall Churn Distribution

## 🛠️ Technologies Used

## 📝 License

This project is licensed under the MIT License.
