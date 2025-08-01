import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime

# Load today's file dynamically
date_str = datetime.now().strftime("%Y-%m-%d")
file_path = fr"C:\Users\sravani\Desktop\ISE\data\temperature_log_{date_str}.csv"

try:
    # Updated to read Humidity column too
    df = pd.read_csv(file_path, names=["Timestamp", "VaccineID", "VaccineName", "Temperature", "Humidity"])
except FileNotFoundError:
    st.error(f"No temperature log found for today ({date_str}).")
    st.stop()

# Convert Timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Vaccine selection dropdown
vaccine = st.selectbox("Select Vaccine", df["VaccineName"].unique())
filtered = df[df["VaccineName"] == vaccine].copy()

# Categorize temperature readings
filtered["Temp Status"] = filtered["Temperature"].apply(lambda t: "Normal" if 2.0 <= t <= 8.0 else "Out of Range")

# Categorize humidity readings
filtered["Humidity Status"] = filtered["Humidity"].apply(lambda h: "Normal" if 30.0 <= h <= 60.0 else "Out of Range")

st.title(f"Temperature & Humidity Log for {vaccine}")

# Temperature chart
temp_line = alt.Chart(filtered).mark_line(color='gray').encode(
    x=alt.X("Timestamp:T", title="Time", axis=alt.Axis(format="%H:%M:%S")),
    y=alt.Y("Temperature:Q", title="Temperature (°C)")
)

temp_points = alt.Chart(filtered).mark_circle(size=60).encode(
    x="Timestamp:T",
    y="Temperature:Q",
    color=alt.Color("Temp Status:N", scale=alt.Scale(domain=["Normal", "Out of Range"], range=["green", "red"]), legend=None),
    tooltip=[
        alt.Tooltip("Timestamp:T", title="Timestamp", format="%Y-%m-%d %H:%M:%S"),
        alt.Tooltip("Temperature:Q", title="Temperature (°C)"),
        alt.Tooltip("Temp Status:N", title="Status")
    ]
)

temp_chart = (temp_line + temp_points).properties(width=700, height=300).interactive()

# Humidity chart
humidity_line = alt.Chart(filtered).mark_line(color='gray').encode(
    x=alt.X("Timestamp:T", title="Time", axis=alt.Axis(format="%H:%M:%S")),
    y=alt.Y("Humidity:Q", title="Humidity (%)")
)

humidity_points = alt.Chart(filtered).mark_circle(size=60).encode(
    x="Timestamp:T",
    y="Humidity:Q",
    color=alt.Color("Humidity Status:N", scale=alt.Scale(domain=["Normal", "Out of Range"], range=["blue", "orange"]), legend=None),
    tooltip=[
        alt.Tooltip("Timestamp:T", title="Timestamp", format="%Y-%m-%d %H:%M:%S"),
        alt.Tooltip("Humidity:Q", title="Humidity (%)"),
        alt.Tooltip("Humidity Status:N", title="Status")
    ]
)

humidity_chart = (humidity_line + humidity_points).properties(width=700, height=300).interactive()

# Display charts
st.subheader("Temperature Monitoring")
st.altair_chart(temp_chart)

st.subheader("Humidity Monitoring")
st.altair_chart(humidity_chart)

# Latest readings check
latest_temp = filtered["Temperature"].iloc[-1]
latest_temp_time = filtered["Timestamp"].iloc[-1].strftime("%H:%M:%S")

latest_humidity = filtered["Humidity"].iloc[-1]
latest_humidity_time = filtered["Timestamp"].iloc[-1].strftime("%H:%M:%S")

# Temperature alert
if latest_temp < 2 or latest_temp > 8:
    st.markdown(f"""
    <div style="padding:15px; background-color:#ff4b4b; color:white; font-size:20px; font-weight:bold; border-radius:8px; text-align:center; margin-top:20px;">
        🚨 Temperature breach detected at {latest_temp_time}! Latest reading: {latest_temp}°C
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div style="padding:15px; background-color:#4caf50; color:white; font-size:20px; font-weight:bold; border-radius:8px; text-align:center; margin-top:20px;">
        ✅ Temperature within range at {latest_temp_time}. Latest reading: {latest_temp}°C
    </div>
    """, unsafe_allow_html=True)

# Humidity alert
if latest_humidity < 30 or latest_humidity > 60:
    st.markdown(f"""
    <div style="padding:15px; background-color:#ff9800; color:white; font-size:20px; font-weight:bold; border-radius:8px; text-align:center; margin-top:20px;">
        ⚠️ Humidity breach detected at {latest_humidity_time}! Latest reading: {latest_humidity}%
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div style="padding:15px; background-color:#2196f3; color:white; font-size:20px; font-weight:bold; border-radius:8px; text-align:center; margin-top:20px;">
        ✅ Humidity within range at {latest_humidity_time}. Latest reading: {latest_humidity}%
    </div>
    """, unsafe_allow_html=True)
