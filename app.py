import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(
    page_title="Climate Change Indicators",
    page_icon="🌍",
    layout="centered",
)

# Title of the web app
st.title("🌍 Climate Change Indicators")

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/zz19990220/T510Inclass2/main/climate_change_indicators.csv")

# Display an overview of the dataset
st.markdown("""
This dataset contains various indicators of climate change, including temperature anomalies, CO2 levels, and more. Here's a brief overview of what each column represents:

- `Year`: The year of the recorded data.
- `CO2`: Carbon dioxide levels in the atmosphere.
- ... (Continue this section based on the actual columns in your dataset)
""")

# Define filters in the sidebar
with st.sidebar:
    st.header("Filter Options")
    
    # Slider for filtering by year
    year_range = st.slider(
        "Year",
        int(df["Year"].min()),  # Ensure int type
        int(df["Year"].max()),
        (int(df["Year"].min()), int(df["Year"].max()))  # Set a range as the default value
    )
    
    # Select which indicator to visualize
    indicator_filter = st.selectbox(
        "Indicator",
        options=list(df.columns[1:])  # Assuming the first column is 'Year'
    )
    
    # Slider to select the number of rows to display, default to showing 5 rows
    row_display = st.slider("Number of Rows to Display", 1, len(df), 5)

# Apply filters to the data
# Filter by selected year range
df_filtered = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]

# Display filtered data
st.header("Filtered Data and Visualization")
st.dataframe(df_filtered.head(row_display))

# Visualization with Plotly Express
fig = px.line(df_filtered, x="Year", y=indicator_filter, title=f"{indicator_filter} over Time")
st.plotly_chart(fig)

# Add an expander to show the raw data on demand
with st.expander("View RAW Data"):
    st.write(df)
