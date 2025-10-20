import subprocess
import platform
import datetime
import sys
import re

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def command():
    if platform.system().lower().startswith("win"):
        cmd = "query user"
    else:
        cmd = "who"
    return cmd

def main():
    cmd = command()
    filename = f"session_tracker_{date}.txt"
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=5)
        username = re.findall(r">(\S+)", result.stdout)
        
        with open(filename, "w") as f:
            f.write("=== USER CHECK ===\n")
            f.write(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}\n")
            f.write(f"Command: {cmd}\n")
            f.write("-------\n")
            if username:
                f.write(f"Username: {username[0]}\n")
            else:
                f.write("No output was returned.\n")
            if result.stderr:
                f.write("\n")
                f.write("Errors:\n")
                f.write(f"{result.stderr.strip()}\n")
            f.write("")
            f.write(f"Exit Code: {result.returncode}\n")
            f.write("==================\n")

    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
  