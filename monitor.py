import random
import csv
from datetime import datetime

# Temperature thresholds
MIN_TEMP = 2.0
MAX_TEMP = 8.0

# Humidity thresholds
MIN_HUMIDITY = 30.0
MAX_HUMIDITY = 50.0

def simulate_temperature():
    # 90% chance to be normal, 10% chance to be out of range
    if random.random() < 0.9:
        return round(random.uniform(MIN_TEMP, MAX_TEMP), 2)
    else:
        if random.random() < 0.5:
            return round(random.uniform(0.0, MIN_TEMP - 0.1), 2)
        else:
            return round(random.uniform(MAX_TEMP + 0.1, 12.0), 2)

def simulate_humidity():
    # 90% chance normal, 10% chance out of range
    if random.random() < 0.9:
        return round(random.uniform(MIN_HUMIDITY, MAX_HUMIDITY), 2)
    else:
        if random.random() < 0.5:
            return round(random.uniform(10.0, MIN_HUMIDITY - 1), 2)
        else:
            return round(random.uniform(MAX_HUMIDITY + 1, 70.0), 2)

def simulate_environment():
    temp = simulate_temperature()
    humidity = simulate_humidity()
    return temp, humidity

def log_environment(vaccine_id, vaccine_name, temp, humidity):
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file_path = fr"C:\Users\sravani\Desktop\ISE\data\temperature_log_{date_str}.csv"
    with open(log_file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), vaccine_id, vaccine_name, temp, humidity])

def is_temp_in_range(temp):
    return MIN_TEMP <= temp <= MAX_TEMP

def is_humidity_in_range(humidity):
    return MIN_HUMIDITY <= humidity <= MAX_HUMIDITY

def is_environment_ok(temp, humidity):
    return is_temp_in_range(temp) and is_humidity_in_range(humidity)
