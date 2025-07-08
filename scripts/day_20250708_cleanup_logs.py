import os 
import sys
from datetime import datetime, timedelta
import logging

log_file = f"os.path.basename(__file__).replace('py','').log"""

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename = log_file,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s")

def log_and_print(message, level=logging.INFO):
    logging.log(level, message)
    print(message)

def cleanup_logs(directory):
    now = datetime.now()
    cutoff = now - timedelta(days=7)

    for file in os.listdir(directory):
        file_path = os.join(directory, file)
        if os.path.isfile(file_path) and file.endswith(".log"):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_mtime < cutoff:
                try:
                    os.remove(file_path)
                    log_and_print(f" Deleted old log file: {file_path}")
                except Exception as e:
                    log_and_print(f"Error deleting {file_path}: {e}", level=logging.ERROR)