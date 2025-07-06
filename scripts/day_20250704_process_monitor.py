import psutil
import logging
from datetime import datetime
import os

# Configuration
TOP_N = 5
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

# Logging setup
log_file = f"logs/{os.path.basename(__file__).replace('.py','')}.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename = log_file,
    level = logging.INFO,
    format = "%(asctime)s -%(levelnmae)s - %(message)s)"
)

def log_and_print(message, process):
    print(message)
    logging.info(message)
    if process.cpu_percent() > CPU_THRESHOLD:
        logging.warning(f"⚠️ High CPU usage by {process.name()} (PID {process.pid})")

    if process.memory_percent() > MEM_THRESHOLD:
        logging.warning(f"⚠️ High Memory usage by {process.name()} (PID {process.pid})")
    print(message)


#function to process monitoring 

def process_monitoring():

#List all the processes:
    process = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            process.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    # Sort processes by CPU usage
    top_process = process.sort(process ,key = lambda x: x['cpu_percent'], reverse=True)[:TOP_N]
    log_and_print(f"Top {TOP_N} processes by CPU usage:", level="info")

    for proc in top_process:
        proc.cpu_percent(interval = 0.1)
        log_and_print(f"Process: {proc['name']} (PID: {proc['pid']}) - CPU: {proc['cpu_percent']}% - Memory: {proc['memory_percent']}%", proc)   

if __name__ == "__main__":
    log_and_print("Starting process monitoring script...", None)
    process_monitoring()
    log_and_print("Process monitoring script completed successfully.", None)
