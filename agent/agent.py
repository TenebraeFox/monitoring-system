import psutil
import requests
import time
import socket

SERVER_URL = "http://<SERVER_IP>:5000/api/metrics"
AGENT_ID = socket.gethostname()

def collect_metrics():
    cpu_load = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().used / (1024 * 1024)  # MB
    disk_usage = psutil.disk_usage('/').percent
    return {
        "agent_id": AGENT_ID,
        "cpu_load": cpu_load,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage
    }

if __name__ == '__main__':
    while True:
        metrics = collect_metrics()
        try:
            response = requests.post(SERVER_URL, json=metrics)
            print(f"Sent metrics: {metrics}, Status: {response.status_code}")
        except Exception as e:
            print(f"Failed to send metrics: {e}")
        time.sleep(5)
