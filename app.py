import streamlit as st
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
)

# Title of the web app
st.title("🐧 Penguins Explorer")

# Custom CSS to inject into the Streamlit app
st.markdown("""
    <style>
        .stSlider > div > div > div.css-1hy3cdp {
            background: blue;
        }
        .stSlider > div > div > div:nth-child(2) {
            background: #e6e6e6;
        }
    </style>
    """, unsafe_allow_html=True)

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

# Define filters in the sidebar
with st.sidebar:
    st.header("Filter Options")
    # Slider for filtering by bill length with given min and max values and default range
    bill_length_range = st.slider(
        "Bill Length (mm)",
        32.1,  # Min value
        59.6,  # Max value
        (32.1, 59.6)  # Default range
    )
    # ... rest of your code
