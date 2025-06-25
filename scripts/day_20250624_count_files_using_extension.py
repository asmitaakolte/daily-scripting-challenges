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
def count_extensions(directory):
    extension_count = defaultdict(int)

    if not os.path.exists(directory):
        log_and_print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            ext = ext.lower() or "no_extension"
            extension_count[ext] += 1

    log_and_print(f"\n Extension summary for '{directory}':")
    for ext, count in sorted(extension_count.items()):
        log_and_print(f"{ext} -> {count} file(s)")

def main():
    target_folder = "scripts"
    log_and_print(f"Counting files in '{target_folder}'...")
    count_extensions(target_folder)
    log_and_print("Script completed successfully.\n")

if __name__ == "__main__":
    main()
