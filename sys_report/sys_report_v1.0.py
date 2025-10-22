import subprocess

def sys_check():
    systeminfo = subprocess.run("systeminfo", capture_output=True, check=False, text=True, timeout=5)
    print("==============================")
    for line in systeminfo.stdout.splitlines():
        if "Host Name:" in line:
            parts = line.split(":")
            print(f"Hostname: {parts[1].strip()}")
        if "OS Name:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "OS Version:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "System Manufacturer:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "System Model:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "System Type:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "Processor(s):" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "Domain:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "Total Physical Memory:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "Available Physical Memory:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
    print("==============================")

sys_check()