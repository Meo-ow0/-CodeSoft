import streamlit as st
import joblib

st.title("🎬 Movie Rating Forecaster")
year = st.slider("Release Year", 1990, 2026, 2020)
duration = st.number_input("Duration (minutes)", 60, 200)
# Add a dropdown that maps 'Action' to a number internally
genre = st.selectbox("Genre", ["Action", "Drama", "Comedy"]) 

if st.button("Predict Rating"):
    # Map inputs to the codes the model expects
    prediction = model.predict([[year, duration, ...]])
    st.success(f"The predicted rating is: {prediction[0]:.1f}")