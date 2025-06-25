import os

from collections import defaultdict
from datetime import datetime

# ----- Logging Setup -----
log_file = f"logs/{os.path.basename(__file__).replace('.py', '')}.log"
os.makedirs("logs", exist_ok=True)      
import logging
logging.basicConfig(    
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)   

def log_and_print(message):
    print(message)
    logging.info(message)       
    # ----- Main Logic -----

def find_largest_files(directory, n=5):
    file_sizes = []
    if not os.path.exists(directory):
        log_and_print(f"Directory '{directory}' does not exist.")
        return []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            file_sizes.append((filename, size))
    
    # Sort files by size in descending order
    file_sizes.sort(key=lambda x: x[1], reverse=True)

    largest_files = file_sizes[:n]
    
    log_and_print(f"\nLargest {n} files in '{directory}':")
    for filename, size in largest_files:
        log_and_print(f"{filename} -> {size / (1024 * 1024):.2f} MB")       
    return largest_files

