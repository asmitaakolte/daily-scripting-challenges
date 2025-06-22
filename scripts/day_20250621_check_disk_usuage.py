import shutil

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")

    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)
    percent_used = (used / total) * 100

    print(f"Total Disk: {total_gb} GB")
    print(f"Used Disk: {used_gb} GB")
    print(f"Free Disk: {free_gb} GB")

    if percent_used > 80:
        print("⚠️ Warning: Disk usage exceeds 80%!")
    else:
        print(f"Disk usage is {percent_used:.2f}%, which is within safe limits.")

if __name__ == "__main__":
    check_disk_usage()
