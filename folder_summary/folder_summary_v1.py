# folder summary tool v1.0
import os
import sys
import platform
from datetime import datetime

def system_summary():
    machine_type = platform.system()
    machine_version = platform.release()
    print(f"System: {machine_type} {machine_version}")
    print("Welcome to Folder Summary Tool v1.0")
    print("Please provide your folder path to begin summarization.")
    print("Type 'q' to exit at anytime.\n")

def get_path():
    while True:
        answer = input("Folder path: ")
        if answer.lower() == "q":
            sys.exit()
        verify = input(f"Confirm path <{answer}>? (Y/N)\n")
        if verify.lower() == "q":
            sys.exit()
        elif verify.lower() == "y":
            return answer

def folder_len(confirmed_path):
    file = 0
    dirs = 0
    try:
        for o in os.listdir(confirmed_path):
            full_path = os.path.join(confirmed_path, o)
            if os.path.isfile(full_path):
                file += 1
            elif os.path.isdir(full_path):
                dirs += 1
        return file, dirs, confirmed_path
    except Exception as e:
        print(f"{e}\nPlease verify the folder path and try again.")

def summary_report(a, b, c):
    filename = f"summary_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    answer1 = input(f"This folder contains {a} files and {b} directories.\n" \
    "Would you like to export this data? (Y/N)\n")
    if answer1.lower() == "y":
        with open(filename, "w") as f:
            f.write("Path requested - {}\nFiles: {}\nDirectories: {}".format(c,a,b))
            print("File written successfully!")
            print("Re-initializing...")
    else:
        print("Re-initializing...")

def main():
    system_summary()
    while True:    
        system_path = get_path()
        result = folder_len(system_path)
        if result:
            file, dirs, confirmed_path = result
            summary_report(file, dirs, confirmed_path)

if __name__ == "__main__":
    main()