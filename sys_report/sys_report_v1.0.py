import subprocess

def sys_overview():
    systeminfo = subprocess.run("systeminfo", capture_output=True, check=False, text=True, timeout=5)
    print("===SYSTEM OVERVIEW===========================")
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
            print(f"{parts[0]}: {parts[1].strip().lower()}")
        if "Total Physical Memory:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")
        if "Available Physical Memory:" in line:
            parts = line.split(":")
            print(f"{parts[0]}: {parts[1].strip()}")

def disk_overview():
    result = subprocess.run("wmic logicaldisk get caption,freespace,size", capture_output=True, text=True, check=False, timeout=5)
    print("===DISK USAGE===========================")
    for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if f"{d}:" in result.stdout:
            for line in result.stdout.splitlines():
                if f"{d}:" in line:
                    parts = line.split()
                    if len(parts) >= 3:
                        drive, free, size = parts[0], parts[1], parts[2]
                        try:
                            free_gb = int(free) / (1024**3)
                            size_gb = int(size) / (1024**3)
                            print(f"{drive} {free_gb:.2f} GB / {size_gb:.2f} GB")
                        except (ValueError, ZeroDivisionError):
                            pass
    print("==============================")

def main():
    sys_overview()
    disk_overview()

if __name__ == "__main__":
    main()