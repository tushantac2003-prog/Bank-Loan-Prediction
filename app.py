import streamlit as st
import pickle
import numpy as np

# Load model
with open ("build.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Bank Loan Prediction")

st.write("Enter Applicant Details")

age = st.number_input("Age")
gender = st.selectbox("Gender" , ["Male","Female"])
married = st.selectbox("Married", ["Yes","No"])
dependents = st.selectbox("No of Dependents", ["0","1","2","3+"])
income = st.number_input("ApplicantIncome")
loan_amount = st.number_input("LoanAmount")
credit_history = st.selectbox("Previous_Loan_Taken",["Yes","No"])
cibil_score = st.number_input("Cibil_Score")
property_area = st.selectbox("Property_Area", ["Urban","Rural","Semiurban"])

if st.button("Predict Loan Status"):

    credit_history = 1 if credit_history == "Yes" else 0
    married = 1 if married=="Yes" else 0
    property_area_map = {"Urban":2,"Rural":0,"Semiurban":1}
    property_area = property_area_map[property_area]
    gender = 1 if gender == "Male" else 0
    dependents_map = {"0":0, "1":1, "2":2, "3+":3}
    dependents = dependents_map[dependents]

    features = np.array([[income, loan_amount, cibil_score, dependents, credit_history,property_area, age, married, gender]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
