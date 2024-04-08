import streamlit as st
import pandas as pd
import altair as alt  # For data visualization

# Set Streamlit page configuration
st.set_page_config(
    page_title="Dog Information",
    page_icon="🐶",
    layout="centered",
)

# Title and overview of the web app
st.title("🐶 Dog Information Dashboard")
st.markdown("""
This dashboard provides insights into various dog breeds, including their height, weight, and suitable environment.
Use the filters on the left to customize the data view.
""")

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/zz19990220/T510Inclass2/main/dog.csv")

# Define filters in the sidebar
with st.sidebar:
    st.header("Filter Options")
    # Slider for filtering by height
    height_range = st.slider(
        "Height (cm)",
        float(df["height_cm"].min()),  # Ensure float type
        float(df["height_cm"].max()),
        (float(df["height_cm"].min()), float(df["height_cm"].max()))  # Set a range as the default value
    )
    
    # Selectbox for selecting breed, with an option to select all
    breed_filter = st.selectbox(
        "Breed",
        options=["All"] + list(df["breed"].unique())
    )
    
    # Multiselect for selecting environment, default to all selected
    environment_filter = st.multiselect(
        "Environment",
        options=list(df["environment"].unique()),
        default=list(df["environment"].unique())
    )

    # Multiselect for selecting which columns to display, default to all selected
    columns_to_display = st.multiselect(
        "Select columns to display",
        options=list(df.columns),
        default=list(df.columns)
    )
