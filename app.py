import streamlit as st
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

# Load data
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Data Preview:")
    st.write(data.head())

    # Preprocess data
    data['step'] = pd.to_datetime(data['step'], unit='d', origin='unix')
    data.set_index('step', inplace=True)

    # Filter only fraud transactions
    fraud_data = data[data['isFraud'] == 1]

    st.write("Fraud Data Preview:")
    st.write(fraud_data.head())

    # Build model
    fraud_counts = fraud_data.resample('D').size()
    model = ExponentialSmoothing(fraud_counts, seasonal='add', seasonal_periods=7)
    model_fit = model.fit()

    # Make predictions
    future_steps = st.slider('Select number of future steps for prediction', 1, 30, 7)
    forecast = model_fit.forecast(steps=future_steps)

    st.write("Fraud Forecast:")
    st.write(forecast)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(fraud_counts, label='Observed')
    plt.plot(forecast, label='Forecast', color='red')
    plt.title('Fraud Detection Forecast')
    plt.xlabel('Date')
    plt.ylabel('Number of Fraudulent Transactions')
    plt.legend()
    st.pyplot(plt)
