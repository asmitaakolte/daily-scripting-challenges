import os 
import logging
import psutil
from datetime import datetime

# ----- Logging Setup -----
log_file = f"logs/{os.path.basename(__file__).replace('.py','')}.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level = logging.INFO,
    format= "%(asctime)s - %(levelnmae)s - %(message)s"   
)

def log_and_print(message, level="info"):
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)    
    elif level == "error":
        logging.error(message)
    print(message)

# ----- Main Logic -----
def disk_memory_usuage():
    memory_percentage = psutil.disk_usage('/').percent

    if memory_percentage > 75:
        log_and_print(f"Disk usage is high: {memory_percentage}%", level="warning")
    else:
        log_and_print(f"Disk usage is normal: {memory_percentage}%", level="info")

if __name__ == "__main__":
    log_and_print("Starting disk usage monitoring script...")
    disk_memory_usuage()
    log_and_print("Disk usage monitoring script completed successfully.")   
