from config import VACCINES
from monitor import simulate_environment, log_environment, is_environment_ok
from escalation import handle_alert
import time

def monitor_loop():
    while True:
        for vaccine in VACCINES:
            temp, humidity = simulate_environment()
            log_environment(vaccine["id"], vaccine["name"], temp, humidity)
            print(f"[{vaccine['name']}] Temperature: {temp}°C, Humidity: {humidity}%")

            if not is_environment_ok(temp, humidity):
                print(f"[ALERT] {vaccine['name']} conditions out of range!")
                handle_alert(vaccine["name"], temp, humidity)

        time.sleep(5)

if __name__ == "__main__":
    monitor_loop()
