import streamlit as st
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(
    page_title="Dog",
    page_icon="🦩",
    layout="centered",
)

# Title of the web app
st.title("🦩 Dog”)

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/zz19990220/T510Inclass2/main/dog.csv")

# Define filters in the sidebar
with st.sidebar:
    st.header("Filter Options")
    # Slider for filtering by bill length
    bill_length_range = st.slider(
        "Bill Length (mm)",
        float(df["bill_length_mm"].min()),  # Ensure float type
        float(df["bill_length_mm"].max()),
        (float(df["bill_length_mm"].min()), float(df["bill_length_mm"].max()))  # Set a range as the default value
    )
    
    # Selectbox for selecting species, with an option to select all
    species_filter = st.selectbox(
        "Species",
        options=["All"] + list(df["species"].unique())
    )
    
    # Multiselect for selecting islands, default to all selected
    islands_filter = st.multiselect(
        "Island",
        options=list(df["island"].unique()),
        default=list(df["island"].unique())
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
# Filter by selected species if not 'All'
if species_filter != "All":
    df = df[df["species"] == species_filter]

# Filter by selected islands
if islands_filter:
    df = df[df["island"].isin(islands_filter)]

# Filter by bill length using the range slider
df = df[(df["bill_length_mm"] >= bill_length_range[0]) & (df["bill_length_mm"] <= bill_length_range[1])]

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
