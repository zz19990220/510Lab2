import streamlit as st
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(
    page_title="Dogs",
    page_icon="🐕",
    layout="centered",
)

# Title of the web app
st.title("🐕 Dogs")

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/zz19990220/T510Inclass2/main/dog.csv") 

# Define filters in the sidebar
with st.sidebar:
    st.header("Filter Options")
    # Slider for filtering by weight
    weight_range = st.slider(
        "Weight (kg)",
        float(df["weight_kg"].min()),
        float(df["weight_kg"].max()),
        (float(df["weight_kg"].min()), float(df["weight_kg"].max()))
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

    # Slider to select the number of rows to display, default to showing 5 rows
    row_display = st.slider("Number of Rows to Display", 1, len(df), 5)

# Apply filters to the data
# Filter by selected breed if not 'All'
if breed_filter != "All":
    df = df[df["breed"] == breed_filter]

# Filter by selected environment
if environment_filter:
    df = df[df["environment"].isin(environment_filter)]

# Filter by weight using the range slider
df = df[(df["weight_kg"] >= weight_range[0]) & (df["weight_kg"] <= weight_range[1])]

# Display filtered data
st.header("Filtered Data")
# Make sure to only display selected columns and handle case when no columns are selected
if columns_to_display:
    st.dataframe(df[columns_to_display].head(row_display))
else:
    st.write("No columns selected. Please select columns to display.")

# Add an expander to show the raw data on demand
with st.expander("View RAW Data"):
    st.write(df)
