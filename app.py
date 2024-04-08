import streamlit as st
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(
    page_title="Dog",
    page_icon="🐶",
    layout="centered",
)

# Title of the web app
st.title("🐶 Dog Breeds")

# Load the dog dataset
dog_df = pd.read_csv("https://raw.githubusercontent.com/zz19990220/T510Inclass2/main/dog.csv")

# Sidebar filters
with st.sidebar:
    st.header("Filter Options")
    selected_breed = st.selectbox("Select Breed", dog_df["breed"].unique())
    selected_environment = st.selectbox("Select Environment", dog_df["environment"].unique())
    selected_sex = st.selectbox("Select Sex", dog_df["sex"].unique())

# Filter the dataset based on user selections
filtered_dogs = dog_df[
    (dog_df["breed"] == selected_breed)
    & (dog_df["environment"] == selected_environment)
    & (dog_df["sex"] == selected_sex)
]

# Display filtered results
st.write(f"Showing {len(filtered_dogs)} {selected_sex} {selected_breed}s in a {selected_environment} environment:")
st.dataframe(filtered_dogs)
