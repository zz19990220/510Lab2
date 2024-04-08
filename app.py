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

# Overview of the dataset
st.markdown("""
This dataset contains information about various breeds of dogs. Here's what each column represents:
- **Breed**: The breed of the dog
- **Environment**: The environment where the dog is commonly found (Urban, Suburban, Rural)
- **Height_cm**: The average height of the dog in centimeters
- **Weight_kg**: The average weight of the dog in kilograms
- **Lifespan_years**: The average lifespan of the dog in years
- **Temperament**: The common temperament of the dog
- **Sex**: The sex of the dog (Male, Female)
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
# Filter by selected breed if not 'All'
if breed_filter != "All":
    df = df[df["breed"] == breed_filter]

# Filter by selected environment
if environment_filter:
    df = df[df["environment"].isin(environment_filter)]

# Filter by height using the range slider
df = df[(df["height_cm"] >= height_range[0]) & (df["height_cm"] <= height_range[1])]

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

# Data visualization
st.header("Data Visualization")

# Bar chart for breed distribution
st.subheader("Breed Distribution")
breed_counts = df["breed"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=breed_counts.index, y=breed_counts.values, palette="viridis", ax=ax)
plt.xticks(rotation=90)
plt.xlabel('Breed')
plt.ylabel('Count')
plt.title('Breed Distribution')
st.pyplot(fig)

# Histogram for height distribution
st.subheader("Height Distribution")
fig, ax = plt.subplots()
sns.histplot(df["height_cm"], bins=20, color='skyblue', edgecolor='black', ax=ax)
plt.xlabel('Height (cm)')
plt.ylabel('Count')
plt.title('Height Distribution')
st.pyplot(fig)

# Boxplot for weight distribution by breed
st.subheader("Weight Distribution by Breed")
fig, ax = plt.subplots()
sns.boxplot(x="breed", y="weight_kg", data=df, palette="viridis", ax=ax)
plt.xticks(rotation=90)
plt.xlabel('Breed')
plt.ylabel('Weight (kg)')
plt.title('Weight Distribution by Breed')
st.pyplot(fig)
