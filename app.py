import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page config to customise the Streamlit app
st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
)

# Write the app title and introduction
st.title("Penguins Explorer: A Data Visualization Web App")
st.write("This web app is designed to explore the penguin dataset and visualize "
         "interesting aspects of penguin biology.")

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

# Create interactive widgets for data filtering
bill_length_slider = st.slider(
    "Filter by Bill Length (mm):",
    float(df["bill_length_mm"].min()),
    float(df["bill_length_mm"].max()),
    (float(df["bill_length_mm"].min()), float(df["bill_length_mm"].max()))
)

# Apply filters to dataframe based on user input
df_filtered = df[(df["bill_length_mm"] >= bill_length_slider[0]) & 
                 (df["bill_length_mm"] <= bill_length_slider[1])]

species = st.selectbox("Select Species", options=df["species"].unique())
df_filtered = df_filtered[df_filtered["species"] == species] if species else df_filtered

island = st.multiselect("Select Islands", options=df["island"].unique())
df_filtered = df_filtered[df_filtered["island"].isin(island)] if island else df_filtered

# Display filtered dataframe
st.write(df_filtered)

# Visualize the data with charts
st.subheader("Data Visualization")

# Histogram of bill lengths
st.write("Distribution of Bill Lengths")
fig, ax = plt.subplots()
sns.histplot(df_filtered["bill_length_mm"], bins=20, kde=False, ax=ax)
st.pyplot(fig)

# Scatter plot for bill length vs. flipper length
st.write("Bill Length vs. Flipper Length")
fig, ax = plt.subplots()
sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', hue='species', data=df_filtered, ax=ax)
st.pyplot(fig)

# Use maps if there's geospatial data available (we don't have lat/long for this dataset)
# If you had latitude and longitude data, you could use st.map(df_filtered)

# Reminder to the user to select options from widgets to filter data
st.caption("Use the sliders and dropdown menus above to filter the dataset and update the visualizations.")
