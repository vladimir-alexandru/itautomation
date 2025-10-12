#password auditor v1.0
import time
import sys
import getpass

def startup():
    print("********************************")
    print("Welcome to Password Auditor v1.0")
    print("********************************")
    print("Please input your password for auditing.")
    user_info = getpass.getuser()
    user_start = input(f"Would you like to proceed {user_info}? (y/n)\n")
    if user_start == "y":
        return
    else:
        print("Thank you for choosing Password Auditor!")
        for s in range(3,0,-1):
            print(f"{s}...")
            time.sleep(1)
        sys.exit()


def checker():
    user_input = input("Please input your password.")
    if len(user_input) >= 12:
        len_user = "Correct length confirmed!"
    if "!" in user_input:
        symbols = "Special symbols confirmed!"
    return len_user, symbols

def summary(len_user, symbols):
    print(f"{len_user}\n{symbols}")

def main():
    startup()
    len_user, symbols = checker()
    summary(len_user, symbols)

if __name__ == "__main__":
    main()