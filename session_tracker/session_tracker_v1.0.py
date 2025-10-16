import subprocess
import platform
import datetime
import sys

def command():
    if platform.system().lower().startswith("win"):
        cmd = "query user"
    else:
        cmd = "who"
    return cmd

def main():
    cmd = command()
    try:
        run = subprocess.run(cmd)
        print(run)
    except Exception as e:
        print("Error: ", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
  