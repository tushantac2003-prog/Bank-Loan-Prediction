import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('build.pkl', 'rb'))

st.title("Bank Loan Prediction")

st.write("Enter Applicant Details")

income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
credit_history = st.number_input("Credit History")
dependents = st.number_input("Dependents")

if st.button("Predict Loan Status"):

    features = np.array([[income, loan_amount, credit_history, dependents]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
