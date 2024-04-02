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

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

# Define filters in the sidebar
with st.sidebar:
    st.header("Filter Options")
    # Slider for filtering by bill length
    bill_length_range = st.slider(
        "Bill Length (mm)",
        float(min(df["bill_length_mm"])),  # cast to float to handle slider step issues
        float(max(df["bill_length_mm"])),
        (float(min(df["bill_length_mm"])), float(max(df["bill_length_mm"])))  # Set a range as the default value
    )
    
    # Selectbox for selecting species
    species_filter = st.selectbox(
        "Species",
        options=[None] + list(df["species"].unique()),  # None option for no filter
    )
    
    # Multiselect for selecting islands
    islands_filter = st.multiselect(
        "Island",
        options=list(df["island"].unique()),
    )

    # Multiselect for selecting which columns to display
    columns_to_display = st.multiselect(
        "Select columns to display",
        options=df.columns,
        default=df.columns
    )

    # Slider to select the number of rows to display
    row_display = st.slider("Number of Rows to Display", 1, len(df), 5)

# Apply filters to the data
# Filter by selected species if any
if species_filter:
    df = df[df["species"] == species_filter]

# Filter by selected islands if any
if islands_filter:
    df = df[df["island"].isin(islands_filter)]

# Filter by bill length using the range slider
df = df[(df["bill_length_mm"] >= bill_length_range[0]) & (df["bill_length_mm"] <= bill_length_range[1])]

# Display filtered data
st.header("Filtered Data")
st.dataframe(df[columns_to_display].head(row_display))

# Add an expander to show the raw data on demand
with st.expander("View RAW Data"):
    st.write(df)

