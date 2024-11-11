import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_processing import get_data, filter_data
from utils.prediction import load_model, predict_churn

# Set the page layout to 'wide'
st.set_page_config(layout="wide")

# Load data and model
data = get_data()
model = load_model()

# Sidebar with Filter Options
st.sidebar.header("Filter Options")
gender = st.sidebar.multiselect("Gender", options=data['gender'].unique(), default=[])
internet_service = st.sidebar.multiselect("Internet Service", options=data['InternetService'].unique(), default=[])
contract = st.sidebar.multiselect("Contract", options=data['Contract'].unique(), default=[])

# Apply filters
filtered_data = filter_data(data, gender, internet_service, contract)

# Create three main sections in columns for a left-to-right layout
col1, col2, col3 = st.columns([1, 2, 1.5])

# Column 1: Overview Metrics
with col1:
    st.header("Overview")
    total_customers = data.shape[0]
    churn_rate = data['Churn'].mean() * 100
    avg_monthly_charges = data['MonthlyCharges'].mean()

    st.markdown(f"""
        <div style="color: #1f77b4; font-size: 20px; font-weight: bold;">
            Total Customers: {total_customers}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="color: #e74c3c; font-size: 20px; font-weight: bold;">
            Churn Rate: {churn_rate:.2f}%
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="color: #2ca02c; font-size: 20px; font-weight: bold;">
            Avg Monthly Charges: ${avg_monthly_charges:.2f}
        </div>
    """, unsafe_allow_html=True)

# Column 2: Charts
with col2:
    st.header("Customer Churn Analysis")
    custom_colors = px.colors.qualitative.Vivid

    # Churn rate by Payment Method
    churn_payment = filtered_data.groupby(['PaymentMethod', 'Churn']).size().reset_index(name='Count')
    fig1 = px.bar(churn_payment, x='PaymentMethod', y='Count', color='Churn', barmode='group',
                  title="Churn Rate by Payment Method", color_discrete_sequence=custom_colors)

    # Total Charges by Contract Type
    filtered_data['TotalCharges'] = pd.to_numeric(filtered_data['TotalCharges'], errors='coerce')
    charges_contract = filtered_data.groupby('Contract')['TotalCharges'].sum().reset_index()
    fig2 = px.bar(charges_contract, x='Contract', y='TotalCharges', title="Total Charges by Contract Type",
                  color_discrete_sequence=custom_colors)

    # Avg Monthly Charges by Gender & Senior Citizen
    avg_monthly_charges = filtered_data.groupby(['gender', 'SeniorCitizen'])['MonthlyCharges'].mean().reset_index()
    fig3 = px.bar(
        avg_monthly_charges,
        x='gender',
        y='MonthlyCharges',
        color='SeniorCitizen',
        title="Avg Monthly Charges by Gender & Senior Citizen",
        labels={'MonthlyCharges': 'Monthly Charges ($)', 'gender': 'Gender', 'SeniorCitizen': 'Senior'},
        color_discrete_sequence=custom_colors
    )

    # Churn distribution
    fig4 = px.pie(filtered_data, names='Churn', title="Churn Distribution", color_discrete_sequence=custom_colors)

    # Display charts in two rows within this column
    chart_col1, chart_col2 = st.columns(2)
    chart_col1.plotly_chart(fig1, use_container_width=True)
    chart_col2.plotly_chart(fig2, use_container_width=True)

    chart_col3, chart_col4 = st.columns(2)
    chart_col3.plotly_chart(fig3, use_container_width=True)
    chart_col4.plotly_chart(fig4, use_container_width=True)

# Column 3: Churn Prediction
with col3:
    st.header("Churn Prediction for Individual Customers")

    # Customer selection dropdown
    customer_id = st.selectbox("Select Customer ID for Prediction", data['customerID'].unique())

    if customer_id:
        y_pred, y_proba = predict_churn(customer_id, model)

        st.subheader("Prediction Results (Logistic)")
        prediction_info = f"""
            <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div style="background-color: #a8dadc; padding: 15px; color: #1d3557; font-size: 18px; border-radius: 8px;">
                    Churn Prediction: {'Yes' if y_pred == 1 else 'No'}
                </div>
                <div style="background-color: #f1faee; padding: 15px; color: #1d3557; font-size: 18px; border-radius: 8px;">
                    Churn Probability: {y_proba * 100:.2f}%
                </div>
            </div>
            """
        st.markdown(prediction_info, unsafe_allow_html=True)

        # Display customer attributes
        st.subheader("Customer Attributes")
        customer_data = data[data['customerID'] == customer_id].T.reset_index()
        customer_data.columns = ['Attribute', 'Value']
        customer_data['Value'] = customer_data['Value'].astype(str)
        st.table(customer_data)
