import os

def find_log_files(directory):
    log_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                full_path = os.path.join(root, file)
                log_files.append(full_path)
    return log_files

if __name__ == "__main__":
    folder = "logs"  # Change this to any folder
    logs = find_log_files(folder)

    if logs:
        print("🔍 Found .log files:")
        for f in logs:
            print(f)
    else:
        print("❌ No log files found.")
