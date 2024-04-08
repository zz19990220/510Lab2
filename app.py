# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset (Make sure to download the dataset from Kaggle and update the path accordingly)
DATA_URL = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

# Initialize the app and load data
data = load_data()

# App title and overview
st.title('Water Potability Analysis')
st.markdown("""
This dataset contains information about water quality measured across different locations, focusing on its potability. 
Potability indicates whether the water is safe for human consumption. The dataset includes several parameters such as pH, Hardness, Solids, Chloramines, and others. Here's a brief overview of each column:

- `ph`: pH of 1. water (0 to 14).
- `Hardness`: Capacity of water to precipitate soap in mg/L.
- `Solids`: Total dissolved solids in ppm.
- `Chloramines`: Amount of Chloramines in ppm.
- `Sulfate`: Amount of Sulfates dissolved in mg/L.
- `Conductivity`: Electrical conductivity of water in μS/cm.
- `Organic_carbon`: Amount of organic carbon in ppm.
- `Trihalomethanes`: Amount of Trihalomethanes in μg/L.
- `Turbidity`: Measure of light emitting properties of water in NTU.
- `Potability`: Indicates if water is safe for human consumption. 1 for potable and 0 for not potable.
""")

# Filtering widgets in the sidebar
st.sidebar.header('Filter Data')
parameter = st.sidebar.selectbox('Select parameter to visualize', ('ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'))
potability = st.sidebar.radio('Potability', ('All', 'Potable', 'Not Potable'))

# Filter data based on selection
if potability == 'Potable':
    filtered_data = data[data['Potability'] == 1]
elif potability == 'Not Potable':
    filtered_data = data[data['Potability'] == 0]
else:
    filtered_data = data

# Visualization
fig = px.histogram(filtered_data, x=parameter, color="Potability", barmode="overlay")
st.plotly_chart(fig, use_container_width=True)

# Optional: Advanced layouts for improved UX
st.markdown('### Statistical Overview')
st.write(filtered_data.describe())
