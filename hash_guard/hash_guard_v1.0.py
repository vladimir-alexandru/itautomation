# hash_guard hashes files in a chosen folder to verify integrity & detect changes.
import os
import sys
import time
import getpass
import hashlib
import platform
from datetime import datetime as dt

def startup():
    operating_system = platform.system()
    system_release = platform.release()
    current_user = getpass.getuser()
    current_date = dt.now().strftime('%Y-%m-%d')
    current_time = dt.now().strftime('%H-%M-%S')
    print("--------------------------")
    print("Welcome to Hash Guard v1.0")
    print("--------------------------")
    print(f"OS: {operating_system} {system_release}")
    print(f"User: {current_user}")
    print(f"Date: {current_date}")
    print(f"Time: {current_time}")
    print("--------------------------")
    print("Pick a folder to hash all files and verify integrity.")
    print("Press 'q' to quit at anytime.")

def checker():
    while True:
        user_path = input("Please provide your path: ")
        if user_path.lower().startswith(("c:","/bin", "/boot", "/etc", "/usr", "/root", "/dev", "/proc")):
            print("Path blocked for safety. Do not use root drives.")
            continue
        elif user_path.lower() == "q":
            sys.exit()
        elif os.path.exists(user_path) == True:
            print("--------------------------")
            print(f"Path confirmed! <{user_path}>")
            report_name = f"hash_report_{dt.now().strftime('%Y-%m-%d_%Hh-%Mm-%Ss')}.txt"
            print("Hashing files... please wait.")
            count = 0
            start = time.time()
            for file in os.listdir(user_path):
                final_path = os.path.join(user_path, file)
                if os.path.isfile(final_path):
                    try:
                        with open(final_path, 'rb') as f:
                            hasher = hashlib.sha256()
                            chunk = f.read(4096)
                            while chunk:
                                hasher.update(chunk)
                                chunk = f.read(4096)
                            digest = hasher.hexdigest()
                            with open(report_name, 'a') as report:
                                report.write(f"{file} | {digest}\n")
                                count += 1                       
                    except Exception as e:
                        print(f"Permission Denied: {e}") 
                    
                else:
                    print(f"Skipping folder: {file}")
            end = time.time()
            print(f"Hashed {count} file(s) successfully!")
            print(f"Operation completed in {end - start:.2f} seconds.")
            print(f"{report_name} created in your current working directory.")                     
            print("--------------------------")       
        else:
            print("Invalid path. Please try Again.")

def main():
    startup()
    checker()

if __name__ == "__main__":
    main()