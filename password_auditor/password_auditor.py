#password auditor v1.0
import time
import sys
import getpass

def startup():
    print("Welcome to Password Auditor v1.0")
    print("********************************")
    print("Please input your password for auditing.")
    print("Type 'q' to quit anytime.")
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
    user_input = input("Please input your password.")
    special_chars = [
    "!", '"', "#", "$", "%", "&", "'", "(", ")", "*",
    "+", ",", "-", ".", "/", ":", ";", "<", "=", ">",
    "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|",
    "}", "~"]

    symbol = False
    digit = False
    alpha = False
    lower = False
    upper = False

    for char in user_input:
        if char in special_chars:
            symbol = True
        if char.isdigit():
            digit = True
        if char.isalpha():
            alpha = True
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
    
    if symbol:
        symbol = "Special symbols confirmed!"
    else:
        symbol = "FAIL: Special characters criteria not satisfied."

    if digit:
        digit = "Digit confirmed!"
    else:
        digit = "FAIL: No digits found"   

    if alpha:
        alpha = "Alphanumeric confirmed!"
    else:
        alpha = "FAIL: No alphanumeric character found!"   

    if lower:
        lower = "Lower case characters confirmed!"
    else:
        lower = "FAIL: No lower case characters found!"   
    
    if upper:
        upper = "Upper case characters confirmed!"
    else:
        upper = "FAIL: No upper case characters found!"   

    if len(user_input) >= 12:
        len_user = "Correct length confirmed!"
    else:
        len_user = f"FAIL: Length criteria not satisfied. Password is {len(user_input)} characters long."

    return len_user, symbol, digit, alpha, lower, upper

def summary(len_user, symbol, digit, alpha, lower, upper):
    print("------------------------------------------")
    print(f"{len_user}\n{symbol}\n{digit}\n{alpha}\n{lower}\n{upper}")
    print("------------------------------------------")
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
        len_user, symbol, digit, alpha, lower, upper = checker()
        summary(len_user, symbol, digit, alpha, lower, upper)

if __name__ == "__main__":
    main()