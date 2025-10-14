import os
import sys
import regex

def startup():
    print('Weclome to Log Auditor v1.0')
    user_input = input("Please provide folder path.")
    if os.path.exists(user_input):
        print(f"Path confirmed! <{user_input}>")
        return user_input
    else:
        print("Invalid path. Please try again")

def confirmation():
    print("------------")
    print("1 - INFO\n2 - WARN\n3 - ERROR\n4 - DEBUG\n5 - NOTICE\n6 - CRITICAL")
    print("------------")
    choices = {
    1: "INFO",
    2: "WARN",
    3: "ERROR",
    4: "CRITICAL",
    5: "NOTICE",
    6: "DEBUG"
    }
    
    while True:
        choice = input("What log severity level would you like to parse? ")
        if choice.lower() == "q":
            sys.exit()
        elif choice.isdigit() and int(choice) in range(1, 7):
            parsing = choices[int(choice)]
            return parsing
        elif choice.isalpha() and choice.upper() in choices.values():
            parsing = choice.upper()
            return parsing
        else:
            print("Invalid entry.")
        
def reader(pathway):
    for file in os.listdir(pathway):
        if os.path.isdir(os.path.join(pathway, file)):
            continue
        else:
            print(file)

def main():
    path = startup()
    confirmation()
    reader(path)

if __name__ == "__main__":
    main()