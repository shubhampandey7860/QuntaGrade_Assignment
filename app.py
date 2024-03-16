import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Bank Marketing Dashboard",
    page_icon="📊",
    layout="wide"
)

# Read data from the CSV file
@st.cache_data 
def get_data() -> pd.DataFrame:
    dataset = "input.csv"
    return pd.read_csv(dataset)

df = get_data()




# Display the title
st.title("Bank Marketing Dashboard")

# Display a sample of the data
st.write("Sample data:")
st.dataframe(df.head())

# Create an interactive chart
st.write("Interactive chart:")
fig = px.scatter(df, x="age", y="balance")
st.plotly_chart(fig)
