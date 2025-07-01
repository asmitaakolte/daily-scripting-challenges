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
    level=logging.INFO,
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
        memory_info = psuti().percent
       
        if memory_info > 75:
               log_and_print(f"please check memory usuage,current usage is {memory_info}%")
        time.sleep(interval)
        log_and_print("Memory usage monitoring completed.")
def main():
    log_and_print("Starting memory usage monitoring script...")
    monitor_memory_usuage(interval=5, duration=60)
    log_and_print("Memory usage monitoring script completed successfully.")