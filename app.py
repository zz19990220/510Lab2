import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(
    page_title="Dog Information",
    page_icon="🐶",
    layout="centered",
)

# Title and Overview
st.title("🐶 Dog Information")
st.markdown("""
This dataset provides comprehensive information about various dog breeds, including their height, environment preferences, and other characteristics. Use the sidebar options to filter through the data and discover interesting facts about your favorite dog breeds!
""")

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/zz19990220/T510Inclass2/main/dog.csv")

# Define filters in the sidebar
with st.sidebar:
    st.header("Filter Options")
    height_range = st.slider("Height (cm)", float(df["height_cm"].min()), float(df["height_cm"].max()), 
                             (float(df["height_cm"].min()), float(df["height_cm"].max())))
    breed_filter = st.selectbox("Breed", options=["All"] + list(df["breed"].unique()))
    environment_filter = st.multiselect("Environment", options=list(df["environment"].unique()), default=list(df["environment"].unique()))
    columns_to_display = st.multiselect("Select columns to display", options=list(df.columns), default=list(df.columns))
    row_display = st.slider("Number of Rows to Display", 1, len(df), 5)

# Apply filters
if breed_filter != "All":
    df = df[df["breed"] == breed_filter]
if environment_filter:
    df = df[df["environment"].isin(environment_filter)]
df = df[(df["height_cm"] >= height_range[0]) & (df["height_cm"] <= height_range[1])]

# Display filtered data
st.header("Filtered Data")
if columns_to_display:
    st.dataframe(df[columns_to_display].head(row_display))
else:
    st.write("No columns selected. Please select columns to display.")

# Visualization: Histogram of Dog Heights within the filtered results
st.header("Height Distribution")
fig, ax = plt.subplots()
ax.hist(df["height_cm"], bins=20, color='skyblue')
ax.set_title('Distribution of Dog Heights')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Add an expander to show the raw data on demand
with st.expander("View RAW Data"):
    st.write(df)
