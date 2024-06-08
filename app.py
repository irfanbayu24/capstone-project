import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from translate import Translator

#membaca model
with open('model_rfc.sav', 'rb') as model_file:
    fraud_model = pickle.load(model_file)

#fungsi untuk menerjemahkan teks dengan caching
@st.cache_data
def translate_text(text, dest_language):
    translator = Translator(to_lang=dest_language)
    translation = translator.translate(text)
    return translation

#judul web
def main_page():
    st.title('Online Transactions Guard System')

    languages = {
        'English': 'en',
        'Indonesian': 'id'
    }

    selected_language = st.radio('Select Language', list(languages.keys()))
    dest_language = languages[selected_language]

    col1, col2 = st.columns(2)

    with col1:
        step = st.selectbox(translate_text('Step', dest_language), [1])
    with col1:
        isFraud = st.selectbox(translate_text('Fraud', dest_language), [0, 1])
    with col1:
        oldbalanceOrg = st.number_input(translate_text('Old Balance Original', dest_language), min_value=0.0, max_value=10000000.0)
    with col1:
        oldbalanceDest = st.number_input(translate_text('Old Balance Destination', dest_language), min_value=0.0, max_value=10000000.0)
    with col2:
        amount = st.number_input(translate_text('Amount', dest_language), min_value=0.0, max_value=10000000.0)
    with col2:
        isFlaggedFraud = st.selectbox(translate_text('Flagged Fraud', dest_language), [0, 1])
    with col2:
        newbalanceOrig = st.number_input(translate_text('New Balance Original', dest_language), min_value=0.0, max_value=10000000.0)
    with col2:
        newbalanceDest = st.number_input(translate_text('New Balance Destination', dest_language), min_value=0.0, max_value=10000000.0)

    #code untuk prediksi
    detect_fraud = ''

    #tombol untuk memprediksi
    if st.button(translate_text('Predict Fraud Transaction', dest_language)):
        fraud_prediction = fraud_model.predict([[step, amount, isFraud, isFlaggedFraud, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])

        if fraud_prediction[0] == 1:
            detect_fraud = st.success(translate_text('Transaction is not fraud', dest_language))
        else:
            detect_fraud = st.error(translate_text('Transaction is fraud', dest_language))
    
    # Tambahkan tombol logout
    if st.button(translate_text('Log Out', dest_language)):
        st.session_state.clear()
        st.experimental_rerun()

if __name__ == "__main__":
    main_page()
