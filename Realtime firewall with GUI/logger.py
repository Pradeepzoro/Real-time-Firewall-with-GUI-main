# logger.py
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "firewall.log")

def log_event(packet, action):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        packet_info = packet.summary()
    except Exception:
        packet_info = str(packet)

    log_line = f"[{time}] {action} | {packet_info}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_line)
        f.flush()

