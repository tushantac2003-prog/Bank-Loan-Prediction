import streamlit as st
import pickle
import numpy as np

# Load model
with open ("build.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Bank Loan Prediction")

st.write("Enter Applicant Details")

income = st.number_input("ApplicantIncome")
loan_amount = st.number_input("LoanAmount")
cibil_score = st.number_input("Cibil_Score")
dependents = st.selectbox("No of Dependents", ["2","3+"])
credit_history = st.selectbox("Previous_Loan_Taken",["Yes","No"])
property_area = st.selectbox("Property_Area", ["Urban","Rural","Semiurban"])
age = st.number_input("Age")
married = st.selectbox("Married", ["Yes","No"])

if st.button("Predict Loan Status"):

    features = np.array([[income, loan_amount, cibil_score, dependents, credit_history, age, property_area, married]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
