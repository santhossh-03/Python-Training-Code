import  streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="🏥 Hospital Sensor Live Monitor", layout="wide")

st.title("🏥 Hospital Live Sensor Monitor")
st.markdown("Real-time monitoring of patient vital signs")

# Create placeholder for dynamic data
placeholder = st.empty()

# Simulate live data
for i in range(200):
    # Simulated sensor readings
    heart_rate = np.random.randint(60, 100)       # beats per minute
    temperature = np.random.uniform(36.0, 37.5)   # °C
    oxygen_level = np.random.randint(94, 100)     # %
    blood_pressure = f"{np.random.randint(110, 130)}/{np.random.randint(70, 90)}"

    # Create a dashboard layout
    with placeholder.container():
        st.subheader("🔹 Patient Vital Signs")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("💓 Heart Rate (BPM)", heart_rate)
        col2.metric("🌡️ Temperature (°C)", f"{temperature:.1f}")
        col3.metric("🫁 Oxygen Level (%)", oxygen_level)
        col4.metric("🩸 Blood Pressure", blood_pressure)

        # Create chart data
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["Heart Rate", "Temperature", "Oxygen Level"]
        )

        st.line_chart(chart_data)

        st.caption("Updating every second...")

        time.sleep(1)

