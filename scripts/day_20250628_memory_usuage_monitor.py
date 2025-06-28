from time import time
import psutil
import logging
from datetime import datetime
import os

# ----- Logging Setup -----
log_file = f"logs/{os.path.basename(__file__).replace(".py","")}.log"
os.makedirs("logs",exist_ok= True)
logging.basicConfig(
    filename=log_file,
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_and_print(message):
    print(message)
    logging.info(message)
    logging.warning(message)    
    logging.error(message)  

# ----- Main Logic -----
def monitor_memory_usuage(interval=5,duration =60):
    start_time = datetime.now()
    log_and_print(f"Starting memory usage monitoring for {duration} seconds...")

    while (datetime.now() - start_time).seconds < duration:
        memory_info = psutil.virtual_memory()
        used_memory = memory_info.used / (1024 * 1024)(1025 * 1024)  # Convert to 
        total_memory = memory_info.total/ (1024 * 1024)
        memory_usuage_percentage = memory_info.percent
        if memory_usuage_percentage > 75:
                log_and_print(f"Used Memory: {used_memory:.2f} MB, Total Memory: {total_memory:.2f} MB, Usage: {memory_usuage_percentage}%")
        time.sleep(interval)
        log_and_print("Memory usage monitoring completed.")
def main():
    log_and_print("Starting memory usage monitoring script...")
    monitor_memory_usuage(interval=5, duration=60)
    log_and_print("Memory usage monitoring script completed successfully.")