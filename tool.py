# folder summary tool v1.0
import os
import sys
import platform

def system_summary():
    machine_type = platform.system()
    machine_version = platform.release()
    print(f"System: {machine_type} {machine_version}")
    print("Welcome to Folder Summary Tool v1.0")
    print("Please provide folder path to begin summarization.")
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
        print(f"Your folder has {file} files and {dirs} directories.")
    except Exception as e:
        print(f"Please verify the folder path.\n{e}\nPlease try again.")

def main():
    system_summary()
    while True:    
        system_path = get_path()
        folder_len(system_path)

if __name__ == "__main__":
    main()