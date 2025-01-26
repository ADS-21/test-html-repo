import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and encoder
model_path = "model.pkl"
encoder_path = "encoder.pkl"

try:
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    st.success("Model and encoder loaded successfully!")
except FileNotFoundError:
    st.error("Model or encoder file not found. Ensure 'model.pkl' and 'encoder.pkl' are in the same directory.")
    st.stop()

# Input features
st.title("Travel Destination Predictor")
st.markdown("Enter the trip details to get a destination recommendation:")

# Dropdowns and sliders for user input
destination_type = st.selectbox(
    "Select Destination Type:",
    ["Continental", "Domestic", "Mountain", "International", "Beach", "City", "Adventure"]
)
budget = st.slider("Enter your budget (in USD):", min_value=500, max_value=10000, step=100)
num_days = st.slider("Number of Days:", min_value=3, max_value=10, step=1)

# Predict button
if st.button("Predict Destination"):
    try:
        # Encode the destination type
        encoded_input = encoder.transform([[destination_type]])
        encoded_columns = encoder.get_feature_names_out(['Destination Type'])
        encoded_df = pd.DataFrame(encoded_input, columns=encoded_columns)

        # Combine input into a single DataFrame
        input_data = pd.DataFrame({
            "Cost (USD)": [budget],
            "Number of Days": [num_days]
        })
        input_data = pd.concat([input_data, encoded_df], axis=1)

        # Make prediction
        prediction = model.predict(input_data)
        st.success(f"Recommended Destination: {prediction[0]}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
