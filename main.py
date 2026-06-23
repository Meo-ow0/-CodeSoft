import streamlit as st
import joblib
import os

# Load model
current_dir = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(current_dir, 'movie_model.pkl'))

st.set_page_config(page_title="Movie Insight Pro", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #fff1f4 0%, #ffd5dd 100%);
            color: #58111a;
        }

        .stButton button {
            background-color: #ff4d6d;
            color: #fff;
            border-radius: 12px;
            border: none;
            padding: 0.85rem 1.4rem;
            font-weight: 700;
        }

        .stButton button:hover {
            background-color: #ff1a36;
            color: #fff;
        }

        .stTextInput>div>div>input,
        .stNumberInput>div>div>input,
        .stSelectbox>div>div>div>div,
        .stSlider>div>div>div>div > div {
            background: rgba(255, 255, 255, 0.96);
            border: 1px solid rgba(255, 77, 109, 0.2);
            color: #58111a;
        }

        .stTextInput>div>label,
        .stNumberInput>div>label,
        .stSelectbox>div>label,
        .stSlider>div>label {
            color: #58111a;
            font-weight: 700;
        }

        .stMarkdown h1,
        .stMarkdown h2,
        .stMarkdown h3 {
            color: #58111a;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Movie Success Predictor")

# Inputs
movie_name = st.text_input("Enter Movie Title:")
year = st.number_input("Release Year", 1900, 2030, 2024)
duration = st.slider("Duration (minutes)", 60, 200, 120)
genre = st.selectbox("Genre", ["Action", "Drama", "Comedy", "Thriller", "Horror"])

if st.button("Generate Forecast"):
    if movie_name:
        # Prediction
        prediction = model.predict([[year, duration, 0, 100, 0, 0]])

        st.divider()
        st.subheader(f"Analysis for: {movie_name.upper()}")
        st.success(f"Estimated Rating: {prediction[0]:.1f} / 10")
        st.balloons()
    else:
        st.warning("Please enter a movie title to get a forecast.")
