import streamlit as st
import pandas as pd
import sqlite3

st.title("🚓 SecureCheck Dashboard")

# Connect to DB
conn = sqlite3.connect("police_data.db")
query = "SELECT * FROM traffic_stops"
df = pd.read_sql(query, conn)

# Filters
countries = df['country_name'].unique()
selected_country = st.selectbox("Select Country", countries)
filtered = df[df['country_name'] == selected_country]

st.subheader("🔍 Vehicle Logs")
st.dataframe(filtered)

st.subheader("📊 Violation Count")
st.bar_chart(filtered['violation'].value_counts())

st.subheader("⚖️ Arrest Rate")
arrest_rate = filtered['is_arrested'].mean() * 100
st.metric("Arrest Rate (%)", f"{arrest_rate:.2f}")
