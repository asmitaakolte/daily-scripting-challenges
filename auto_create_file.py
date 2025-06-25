from datetime import datetime
import sys
import os 

def main():
    if len(sys.argv)<2:
        print("Usage: python auto_create_file.py <filename>")
        return
    filename = sys.argv[1]

    current_date = datetime.now().strftime('%Y%m%d')

    base_dir = "scripts"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    final_filename = os.path.join(base_dir,f"day_{current_date}_{filename}")

    dir_name = os.path.dirname(final_filename)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open(final_filename, 'w') as f:
         pass
    print(f"File '{final_filename}' created successfully.")

if __name__ == "__main__":
    main()
