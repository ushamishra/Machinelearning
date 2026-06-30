import streamlit as st
import pickle
import pandas as pd

# Load your trained model
with open("total_studycost_predictor_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Tuition Cost Predictor")

# User inputs
country = st.text_input("Country")
city = st.text_input("City")
university = st.text_input("University")
program = st.text_input("Program")
level = st.text_input("Level")
duration = st.number_input("Duration (Years)")


# Predict button
if st.button("Predict Tuition"):
    data = pd.DataFrame([{
        "Country": country,
        "University": university,
        "City": city,
        "Program": program,
        "Level": level,
        "Duration_Years": duration
    }])
    prediction = model.predict(data)[0]
    st.success(f"Predicted Tuition: ${prediction:.2f}")
