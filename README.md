# vaccine-cold-chain-monitoring
## 📦 Project Overview

This project simulates a Cold Chain Monitoring System designed to ensure the safe storage and transportation of vaccines by continuously monitoring **temperature** and **humidity** using simulated IoT sensors. It includes real-time logging, alert handling, escalation logic, and compliance tracking.

## 🌐 Key Features

- 📡 Real-time simulation of temperature and humidity readings
- ⚠️ Incident detection when thresholds are breached
- 📥 Local logging of all sensor data and incidents
- 🚨 Alert escalation if not acknowledged in time
- 📊 Streamlit dashboard (optional) for live visualization
- 📁 CSV-based storage for audit and traceability

## 🧪 Monitored Vaccines

The system monitors the following vaccines:
- Rabies
- Moderna
- Covaxin
- Polio
- Influenza
- Rotavirus
- Varicella
- BCG
- Hepatitis
- DTP

## 📊 Environmental Thresholds

| Parameter     | Acceptable Range   |
|---------------|--------------------|
| Temperature   | 2°C to 8°C         |
| Humidity      | 30% to 50%         |

## 🛠️ How It Works

1. Each vaccine batch is assigned a sensor.
2. Sensors continuously simulate temperature and humidity readings.
3. Readings are logged into CSV files.
4. If any reading is out of range:
   - An alert is generated.
   - If not acknowledged within 20 seconds, it is escalated to a supervisor.
   - The incident is logged for audit.

## 🧾 File Structure
## 🚀 Getting Started

### Requirements
- Python 3.11 or above

### Run the system
```bash
python main.py

### Run Streamlit
Terminal
"your-python-directory" -m streamlit run dashboard.py
