from genericpath import exists
import os
from datetime import datetime
import logging 
from fileinput import filename
import psutil   


# ----- Logging Setup -----
log_file = f"logs/{os.path.basename(__file__).replace('.py', '')}.log"

os.makedirs("logs",exist_ok =True)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format ="%(asctime)s - %(levelname)s - %(message)s"
)

def log_and_print(message, level="info"):
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
# ----- Main Logic -----
def monitor_log_files(directory):
    if not os.path.exists(directory):
        log_and_print(f"Directory '{directory}' does not exists.")
        return 
    
    list_of_log_files = []
    error_files =[]
    List_of_keywords= ["ERROR", "WARNING", "CRITICAL"]
    for filename in os.listdir(directory):
        if filename.endswith(".log"):
            filepath = os.path.join(directory,filename)
            # open file and start form end of the file
            with open(filepath,"r") as f:
                for line in f:
                    currentTime = datetime.now().strftime("%Y-%m-%d")
                    if currentTime in line:
                        for keywords in List_of_keywords:
                            if keywords in line:
                                error_files.append((filepath,line.strip()))

        return error_files

if __name__ == "__main__":
    log_and_print("Starting log file monitoring script...")
    directory = "logs"
    error_files = monitor_log_files(directory)
    
    if error_files:
        log_and_print("Errors found in the following log files:")
        for file, line in error_files:
            log_and_print(f"{file}: {line}")
    else:
        log_and_print("No errors found in log files.")
    
    log_and_print("Log file monitoring script completed successfully.")
                    