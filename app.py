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

# Title and overview of the dataset
st.title("🐶 Dog Information")
st.markdown("""
This dataset contains information about various dog breeds, 
including their size, weight, environment preference, and more. 
Use the filters on the left to explore the dataset.
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

# Visualizing the data if suitable for the dataset
st.header("Data Visualization")
# Check if 'weight_kg' column is selected for display
if "weight_kg" in columns_to_display:
    # Plotting height vs weight
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="height_cm", y="weight_kg", hue="breed", style="environment", ax=ax)
    plt.title("Height vs Weight of Dogs")
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    st.pyplot(fig)

# Add an expander to show the raw data on demand
with st.expander("View RAW Data"):
    st.write(df)
