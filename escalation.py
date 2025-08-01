import time
from datetime import datetime
import pygame

pygame.mixer.init()

def handle_alert(vaccine_name, temp, humidity):
    print(f"[NOTIFY] Alert for {vaccine_name}: Temperature {temp}°C, Humidity {humidity}%")

    # Load and play buzzer sound on loop
    pygame.mixer.music.load(r'C:\Users\sravani\Desktop\ISE\buzzer.mp3')
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    acknowledged = wait_for_acknowledgement(timeout=20)  # 20 seconds timeout

    if acknowledged:
        pygame.mixer.music.stop()  # Stop the buzzer sound
        print(f"[RESPONDED] {vaccine_name} alert acknowledged.")
        log_incident(f"{vaccine_name}: Primary responder handled breach. Temp: {temp}°C, Humidity: {humidity}%")
    else:
        pygame.mixer.music.stop()
        print(f"[ESCALATION] No response for {vaccine_name}. Escalating.")
        log_incident(f"{vaccine_name}: Supervisor notified for unacknowledged breach. Temp: {temp}°C, Humidity: {humidity}%")

def wait_for_acknowledgement(timeout=20):
    print(f"[SYSTEM] Type 'y' to acknowledge within {timeout} seconds:")
    start_time = time.time()
    while time.time() - start_time < timeout:
        # Non-blocking check is tricky in console, but we use input() with a workaround
        # For simplicity, we try to read input but timeout after 1 second and loop
        # This requires running in an environment that supports this properly.
        try:
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getwch()
                if key.lower() == 'y':
                    return True
        except ImportError:
            # If msvcrt not available (non-Windows), fallback to blocking input (will wait indefinitely)
            # You can replace this with more advanced input handling for your environment.
            if input().lower() == 'y':
                return True
        time.sleep(0.1)
    return False

def log_incident(message):
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file_path = fr"C:\Users\sravani\Desktop\ISE\data\incident_log_{date_str}.txt"
    with open(log_file_path, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
