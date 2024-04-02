mport streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
)

st.title("🐧 Penguins Explorer")

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

bill_length_slider = st.slider(
    "Bill Length (mm)",
    min(df["bill_length_mm"]),
    max(df["bill_length_mm"]),
)

df = df[df["bill_length_mm"] > bill_length_slider]

st.selectbox("Species", df["species"].unique())
st.multiselect("Island", df["island"].unique())

st.write(df)

with st.sidebar:
    # Input filter options
    bill_length_slider = st.slider(
        "Bill Length (mm)",
        min(df["bill_length_mm"]),
        max(df["bill_length_mm"]),
    )
    species_filter = st.selectbox(
        "Species",
        df["species"].unique(),
        index=None
    )
    islands_filter = st.multiselect(
        "Island",
        df["island"].unique()
    )

# Filter data
if islands_filter:
    df = df[df["island"].isin(islands_filter)]
if species_filter:
    df = df[df["species"] == species_filter]
df = df[df["bill_length_mm"] > bill_length_slider]

with st.expander("RAW Data"):
    st.write(df)
