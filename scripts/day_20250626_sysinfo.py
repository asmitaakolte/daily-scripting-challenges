import platform
import logging
import os
from datetime import datetime


def get_system_info():
    """Collects and returns system information."""
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "Hostname": platform.node(),
        "Current Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return info


if __name__ == "__main__":
    object = get_system_info()
    print("System Information:")
    for key, value in object.items():
        print(f"{key}: {value}")    