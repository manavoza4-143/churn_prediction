import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure", 0, 72)

phone = st.selectbox("Phone Service", ["Yes", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check",
    "Bank transfer (automatic)", "Credit card (automatic)"
])

monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

if st.button("Predict"):

    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "InternetService": internet,
        "Contract": contract,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json=data
    )

    if response.status_code == 200:
        try:
         result = response.json()
        except:
         st.error("Invalid response from API")
         st.text(response.text)
         st.stop()
    else:
        st.error(f"API Error: {response.status_code}")
        st.text(response.text)
        st.stop()
