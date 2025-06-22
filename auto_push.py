import subprocess   # to run shell programs 
import sys 
from datetime import datetime  # to get timestamp of program getting push in repo 
import os


try:
    today_prefix = f"day_{datetime.now().strftime('%Y%m%d')}_"
    print (today_prefix)

    script_folder = "scripts"
    scripts_today = [f for f in os.listdir(script_folder) if f.startswith(today_prefix) and f.endswith('.py')]

    if not scripts_today:
        print("No scirpt Today")
        exit(1)

    if len(scripts_today) > 1:
        print('multiple scripts for today. Running the first one: ',scripts_today[0])

    script_path = os.path.join(script_folder,scripts_today[0])
    print('Print Running script: {script_path}')

    # Step 1 : eat run the first file in list  
    subprocess.check_call(['python',script_path])
    print("script execute successfully")

    # Step 2 : git add all the changes 
    subprocess.check_call(["git","add","."])

    # Step 3: Prepare commit message with timestamp
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    commit_msg = f"Auto push on {now} for {scripts_today[0]}"
    subprocess.check_call(['git','commit', '-m',commit_msg])

    # Step 4: Push to GitHub 
    subprocess.check_call(["git", "push", "origin", "main"])
    print(" Changes pushed to GitHub successfully!")


except subprocess.CalledProcessError as e :
    print(f"script failed with error: {e}")
    exit(1)
