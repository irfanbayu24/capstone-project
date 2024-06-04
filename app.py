import pickle
import streamlit as st

#membaca model
fraud_model = pickle.load(open('FraudDetect_model.sav', 'rb'))

#judul web
st.title('Fraud Transaction Detection Simple App')

col1, col2 = st.columns(2)

with col1 :
    step = st.sidebar.selectbox('Step', [1])
with col2 :
    amount = st.sidebar.number_input('Amount', min_value=0.0, max_value=10000000.0)
with col1 :
    isFraud = st.sidebar.selectbox('Fraud', [0, 1])
with col2 :
    isFlaggedFraud = st.sidebar.selectbox('Flagged Fraud', [0, 1])
with col1 :
     oldbalanceOrg = st.sidebar.number_input('Old Balance Original', min_value=0.0, max_value=10000000.0)
with col2 :
     newbalanceOrig = st.sidebar.number_input('New Balance Original', min_value=0.0, max_value=10000000.0)
with col1 :
    oldbalanceDest = st.sidebar.number_input('Old Balance Destination', min_value=0.0, max_value=10000000.0)
with col2 :
    newbalanceDest = st.sidebar.number_input('New Balance Destination', min_value=0.0, max_value=10000000.0)


#code untuk prediksi
detect_fraud = ''

#tombol untuk memprediksi
if st.button('Predict Fraud Transaction'):
    fraud_prediction = fraud_model.predict([[step, amount, isFraud, isFlaggedFraud, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])

    if fraud_prediction[0] == 1:
        detect_fraud = 'Transaction is not fraud'
    else:
        detect_fraud = 'Transaction is fraud'

st.success(detect_fraud)