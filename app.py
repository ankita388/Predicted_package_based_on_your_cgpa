import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

# Set the title
st.title("🎓 CGPA to Package Predictor")
st.markdown("Enter your **CGPA** to predict your expected placement package (in LPM).")

# Input box for CGPA
cgpa = st.number_input("📘 Enter your CGPA", min_value=0.0, max_value=10.0, step=0.01)

# Predict button
if st.button("Predict Package"):
    input_data = np.array([[cgpa]])
    prediction = model.predict(input_data)[0]
    st.success(f"💼 Predicted Package: ₹{prediction:.2f} LPM")