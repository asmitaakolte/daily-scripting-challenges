import shutil
import os
import logging
from datetime import datetime

# Configure logging
log_file = f"logs/{os.path.basename(__file__).replace('py','')}.log"

os.makedirs("logs",exist_ok = True)

logging.basicConfig(
    filename = log_file,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def log_and_print(message, level="info"):
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    print(message)

# Function to monitor folder size
def monitor_folder_size(folder_name):
    #check if folder exists
    if not os.path.isdir(folder_name):
        log_and_print(f"Folder '{folder_name}' does not exist.", level="error")
        return
    else:
        log_and_print(f"Monitoring folder: {folder_name}", level="info")
    # Get the size of the folder
    folder_size = 0
    for dirpath , dirnames, filename in os.walk(folder_name):
        for file in filename:
            file_path = os.path.join(folder_name,file)
            if os.path.isfile(file_path):
                folder_size += os.path.getsize(file_path)
    # Convert size to MB
    folder_size_mb = folder_size / (1024 * 1024)
    log_and_print(f"Size of folder '{folder_name}': {folder_size_mb:.2f} MB", level="info")

    if folder_size_mb > 100:  # Threshold set to 100 MB
        log_and_print(f"Warning: Folder size exceeds 100 MB! Current size: {folder_size_mb:.2f} MB", level="warning")

if __name__ == "__main__":
    log_and_print("Starting folder size monitoring script...")
    folder_to_monitor = "scripts"  # Change this to the folder you want to monitor
    monitor_folder_size(folder_to_monitor)
    log_and_print("Folder size monitoring script completed successfully.")