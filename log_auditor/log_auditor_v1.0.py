import os
import sys
from datetime import datetime

def overhead():
    print('Weclome to Log Auditor v1.0')
    print("Type 'q' to quit")
    print("----------------")

def startup():
    while True:    
        user_input = input("Please provide folder path. ").strip().lower()
        if user_input == "q":
            sys.exit()
        if os.path.exists(user_input):
            print(f"Path confirmed! <{user_input}>")
            return user_input
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
        
def reader(pathway, parseway):
    parse_list = []
    for file in os.listdir(pathway):
        final_path = os.path.join(pathway, file)
        if os.path.isdir(final_path):
            continue
        else:
            with open(final_path) as f:
                for line in f:
                    if parseway in line:
                        parse_list.append(line)
    return parse_list
    
def report(parse_list, parsing):
    filename = f"LogAudit_{parsing}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    while True:    
        user_export = input("Would you like to export the results? (y/n) ").strip().lower()
        if user_export == "n":
            sys.exit()
        elif user_export == "y":
            with open(filename, "a") as f:
                for x in parse_list:
                    f.write(x)
            print(f"Success! {filename} saved in your current working directory!")
            
            while True:
                again = input("Would you like to check another folder? (y/n) ").strip().lower()
                if again == "n":
                    sys.exit()
                elif again == "y":
                    return
                else:
                    print("Invalid entry.")
        else:
            print("Invalid entry.")

def main():
    overhead()
    while True:
        path = startup()
        parsing = confirmation()
        parse_list = reader(path, parsing)
        report(parse_list, parsing)

if __name__ == "__main__":
    main()