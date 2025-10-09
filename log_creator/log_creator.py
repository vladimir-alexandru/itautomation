# WARHING! This program will create practice log files on your machine
import os
import sys
import time
import psutil
import getpass
import platform
from datetime import datetime

def startup():
    system = platform.system()
    version = platform.release()
    gb = 1024**3
    user = getpass.getuser()
    print("********************")
    print(f"Machine: {system} {version}\nUser: {user}\nDate: {datetime.now().strftime('%Y-%m-%d (%H-%M-%S)')}")
    print("********************")
    print("***WARNING*** This program will create practice log files on your machine!")
    print("Type 'q' to quit at anytime.\n")
    choice = input("Scan your partition to check available space? (y/n): ")
    if choice.lower() == "y":
        attempts = 4
        while attempts >= 0:        
            partition = input("Which drive would you like to scan? (e.g., C, D)")
            if len(partition) != 1 or not partition.isalpha():
                print("No input provided. Please enter a drive letter.")
                continue
            elif partition.lower() == "q":
                sys.exit()
            elif partition.isalpha():
                try:
                    partition =  f"{partition.lower()}" + r":\\"
                    disk = psutil.disk_usage(partition)
                    print(f"Disk: {disk.total/gb:.2f} GB\nUsed: {disk.used/gb:.2f} GB\nFree: {disk.free/gb:.2f} GB\nPercent: {disk.percent}%")
                    return
                except Exception as e:
                    print(f"{e}\nInvalid partition, please try again.")
                    print(f"You have {attempts} attempts remaining.")
                if attempts == 0:
                    retry = input("Would you like to try again? (y/n): ")
                    if retry.lower() == "y":
                        attempts = 4
                        continue
                    elif retry.lower() == "q":
                        sys.exit()
                    else:
                        sys.exit()
                    return
                attempts -= 1
    elif choice.lower() == "q":
        sys.exit()
    else:
        return

def path_verification():
    tries = 4
    while tries >= 0:
        path = input("Please provide the path.")
        path_confirm = input(f"Confirm {path}? (y/n): ")
        if tries == 0:
            print("No more tries left. Exiting")
            sys.exit()
        elif path_confirm.lower() == "y":
            try:
                os.mkdir(path)
                print("Folder created at path: {}".format(path))
                for i in range(3, 0, -1):
                    if i == 3:
                        print(f"{i}... Initializing the file forge...")
                    elif i == 2:
                        print(f"{i}... Summong 100 log files from the void.")
                    elif i == 1:
                        print(f"{i}... Last disk spin! Creating logs now!")
                    time.sleep(1)
                return
            except:
                print("Folder already exists")    
                print(f"Try again, {tries} tries remaining.")          
        elif path_confirm.lower() == "n":
            print(f"Try again, {tries} tries remaining.")          
        elif path_confirm.lower() == "q":
            sys.exit()
        tries -= 1

def main():
    startup()
    path_verification()

if __name__ == "__main__":
    main()

