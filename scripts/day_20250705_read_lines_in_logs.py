import os 
import logging
from datetime import datetime


# ----- Logging Setup -----
log_file = f"logs/{os.path.basename(__file__).replace('.py','')}.log"
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
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
def read_lines_in_logs():
    basedir ="logs"
    
    for file in os.listdir(basedir):
        filename = os.path.join(basedir, file)
        with open(filename, 'r') as f:
            lines = f.readlines()
            log_and_print(f"File: {file} - Number of lines: {len(lines)}", level="info")

if __name__ == "__main__":
    log_and_print("Starting to read lines in logs...")
    read_lines_in_logs()
    log_and_print("Completed reading lines in logs.")