import streamlit as st
import pickle
import numpy as np

# Load model
pickle.dump(best_model, open("decision_tree_model.pkl", "wb"))

st.title("Bank Loan Prediction")

st.write("Enter Applicant Details")

income = st.number_input("ApplicantIncome")
loan_amount = st.number_input("LoanAmount")
cibil_score = st.number_input("Cibil_Score")
dependents = st.number_input("Dependents")

if st.button("Predict Loan Status"):

    features = np.array([[income, loan_amount, cibil_score, dependents]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
