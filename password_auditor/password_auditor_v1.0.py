#password auditor v1.0
import time
import sys
import getpass

def startup():
    print("--------------------------------")
    print("Welcome to Password Auditor v1.0")
    print("--------------------------------")
    print("Please input your password for auditing.")
    print("Note that your input remains private.")
    print("Type 'q' to quit anytime.\n")
    user_info = getpass.getuser()
    while True:
        user_start = input(f"Would you like to proceed {user_info}? (y/n)\n")
        if user_start.lower() == "q" or user_start.lower() == "n":
            print("Thank you for choosing Password Auditor!")
            print("This program will now terminate.")
            for s in range(3,0,-1):
                print(f"{s}...")
                time.sleep(1)
            sys.exit()
        elif user_start.lower() == "y":
            return
        else:
            print("Invalid entry.\n")

def checker():
    user_input = getpass.getpass(prompt='Please provide your password: ')
    special_chars = [
    "!", '"', "#", "$", "%", "&", "'", "(", ")", "*",
    "+", ",", "-", ".", "/", ":", ";", "<", "=", ">",
    "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|",
    "}", "~"]

    symbol = False
    digit = False
    lower = False
    upper = False

    for char in user_input:
        if char in special_chars:
            symbol = True
        if char.isdigit():
            digit = True
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
    
    if symbol:
        symbol = "PASS: Special character(s) confirmed!"
    else:
        symbol = "FAIL: No special character(s) found."

    if digit:
        digit = "PASS: Digit(s) confirmed!"
    else:
        digit = "FAIL: No digit(s) found!"   

    if lower:
        lower = "PASS: Lower case character(s) confirmed!"
    else:
        lower = "FAIL: No lower case character(s) found!"   
    
    if upper:
        upper = "PASS: Upper case character(s) confirmed!"
    else:
        upper = "FAIL: No upper case character(s) found!"   

    if len(user_input) >= 12:
        len_user = "PASS: Correct length confirmed!"
    else:
        len_user = "FAIL: Length criteria not satisfied (Min 12 characters required)."

    return len_user, symbol, digit, lower, upper

def summary(digit, lower, upper, symbol, len_user):
    print("------------------------------------------")
    print(f"{len_user}\n{symbol}\n{digit}\n{lower}\n{upper}")
    PASS = "PASS"
    pass_count = 0
    for word in len_user, symbol, digit, lower, upper:
        if PASS in word:
            pass_count += 1
    if pass_count <= 3:
        print("Password Level: Weak")
    elif pass_count == 4:
        print("Password Level: Strong!")
    else:
        print("Password Level: Excellent!")         
    print("------------------------------------------")
    while True:    
        user_repeat = input("Would you like to check another password? (y/n)\n")
        if user_repeat.lower() == "q" or user_repeat.lower() == "n":
            print("Thank you for choosing Password Auditor!")
            print("This program will now terminate.")
            for s in range(3,0,-1):
                print(f"{s}...")
                time.sleep(1)
            sys.exit()
        elif user_repeat.lower() == "y":
            return
        else:
            print("Invalid entry.\n")

def main():
    startup()
    while True:
        len_user, symbol, digit, lower, upper = checker()
        summary(digit, lower, upper, symbol, len_user)

if __name__ == "__main__":
    main()