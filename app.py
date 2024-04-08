import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(
    page_title="Dog Information",
    page_icon="🐶",
    layout="centered",
)

# Title of the web app
st.title("🐶 Dog Information")

# Overview of the dataset using Markdown
st.markdown("""
This dataset contains detailed information about various dog breeds, including their height, 
breed characteristics, and preferred living environment. Use the sidebar to filter the data based on breed, 
height, or environment and explore the characteristics of your favorite dogs.
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

    # Slider to select the number of rows to display, default to showing 5 rows
    row_display = st.slider("Number of Rows to Display", 1, len(df), 5)

# Apply filters to the data
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

# Visualization
st.header("Data Visualization")

# If breed was not filtered to 'All', show average height by environment for the selected breed
if breed_filter != "All":
    st.subheader(f"Average Height by Environment for {breed_filter}")
    avg_height = df.groupby('environment')['height_cm'].mean().reset_index()
    sns.barplot(x='environment', y='height_cm', data=avg_height)
    plt.xlabel("Environment")
    plt.ylabel("Average Height (cm)")
    st.pyplot(plt)
else:
    st.write("Select a specific breed to see average height by environment.")

# Add an expander to show the raw data on demand
with st.expander("View RAW Data"):
    st.write(df)
