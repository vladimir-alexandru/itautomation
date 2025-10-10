# WARHING! This program will create practice log files on your machine
import os
import sys
import time
import psutil
import random
import getpass
import platform
from datetime import datetime

def startup():
    system = platform.system()
    version = platform.release()
    gb = 1024**3
    user = getpass.getuser()
    print("********************")
    print(f"Machine: {system} {version}\nUser: {user}\nDate: {datetime.now().strftime('%Y-%m-%d (%H-%M-%S)')}")
    print("********************")
    print("***WARNING*** This program will create 100 practice log files on your machine!")
    print("Type 'q' to quit at anytime.\n")
    choice = input("Scan your partition to check available space? (y/n): ")
    if choice.lower() == "y":
        attempts = 4
        while attempts >= 0:        
            partition = input("Which drive would you like to scan? (e.g., C, D)")
            if len(partition) != 1 or not partition.isalpha():
                print("No input provided. Please enter a drive letter.")
                continue
            elif partition.lower() == "q":
                sys.exit()
            elif partition.isalpha():
                try:
                    partition =  f"{partition.lower()}" + r":\\"
                    disk = psutil.disk_usage(partition)
                    print(f"Disk: {disk.total/gb:.2f} GB\nUsed: {disk.used/gb:.2f} GB\nFree: {disk.free/gb:.2f} GB\nPercent: {disk.percent}%")
                    return
                except Exception as e:
                    print(f"{e}\nInvalid partition, please try again.")
                    print(f"You have {attempts} attempts remaining.")
                if attempts == 0:
                    retry = input("Would you like to try again? (y/n): ")
                    if retry.lower() == "y":
                        attempts = 4
                        continue
                    elif retry.lower() == "q":
                        sys.exit()
                    else:
                        sys.exit()
                    return
                attempts -= 1
    elif choice.lower() == "q":
        sys.exit()
    else:
        return

def path_verification():
    tries = 4
    while tries >= 0:
        path = input("Please provide the path.")
        path_confirm = input(f"Confirm {path}? (y/n): ")
        if tries == 0:
            print("No more tries left. Exiting")
            sys.exit()
        elif path_confirm.lower() == "y":
            try:
                os.mkdir(path)
                print("Folder created at path: {}".format(path))
                for i in range(3, 0, -1):
                    if i == 3:
                        print(f"{i}... Initializing the file forge...")
                    elif i == 2:
                        print(f"{i}... Summong 100 log files from the void.")
                    elif i == 1:
                        print(f"{i}... Last disk spin! Creating logs now!")
                    time.sleep(1)
                return
            except:
                print("Folder already exists")    
                print(f"Try again, {tries} tries remaining.")          
        elif path_confirm.lower() == "n":
            print(f"Try again, {tries} tries remaining.")          
        elif path_confirm.lower() == "q":
            sys.exit()
        tries -= 1

def creation():
    hostnames = ["ubuntu01", "debian-srv1", "centos-node2", "fedora-lab", 
                "archdev", "rhel-backup", "kali01", "mint-desktop", 
                "pop-os", "ubuntu-test", "srv-web01", "srv-db02", "node03"] 
    systems = ["systemd", "kernel", "init", "udevd", "dbus-daemon"]
    authentication = ["sshd", "auth", "usermgr", "login", "su", "sudo"]
    networking = ["netmon", "ufw", "iptables", "dhclient", "networkd", "conntrackd"]
    files = ["filemon", "auditd", "sysmon", "logrotate", "journalctl"]
    jobs = ["cron", "atd", "update", "apt", "dnf", "yum", "snapd"]
    security = ["backup", "clamav", "fail2ban", "rsync", "execmon", "vaultd"]
    levels = ["INFO", "WARN", "ERROR", "CRITICAL", "NOTICE", "DEBUG"]
    oses = ["Linux", "Ubuntu", "Debian", "CentOS", "Fedora", "ArchLinux", "macOS", "Windows", "FreeBSD"]
    messages = [
    "Service ssh started",
    "Accepted password for alice from 192.168.1.22 port 54421",
    "Failed password for invalid user admin from 203.0.113.60 port 55873",
    "Account locked for user bob after 5 failed attempts",
    "File created /home/alice/report_q4.csv by alice",
    "Unexpected file modification /etc/shadow by unknown",
    "Firewall allowed TCP connection from 192.168.1.22 to 22",
    "Firewall blocked TCP connection from 203.0.113.60 to 22",
    "Scheduled job backup.sh executed successfully",
    "Disk I/O error on /dev/sda1 sector 552813",
    "Possible port scan detected from 203.0.113.60",
    "CPU usage stable at 17%, memory 54%",
    "New user created: testuser by admin",
    "User testuser added to sudo group",
    "Multiple failed logins for testuser from 198.51.100.44",
    "Suspicious exec: /bin/nc -e /bin/sh by testuser",
    "Security patch 2025-10 applied successfully",
    "Backup job completed, 1.2GB archived to /mnt/backup/system_20251008.tar.gz",
    "Connection from 10.0.0.15 to 192.168.1.22:443 allowed",
    "File /var/log/auth.log deleted unexpectedly by unknown",
    "Unauthorized configuration change detected in /etc/ssh/sshd_config",
    "User alice changed password successfully",
    "Firewall rule updated: allow outbound DNS to 8.8.8.8",
    "Kernel panic detected on CPU 2",
    "Service apache2 restarted automatically after crash",
    "Cron job cleanup_temp.sh failed with exit code 1",
    "Malware scan completed, 0 threats found",
    "Login attempt for disabled account guest from 172.16.0.45",
    "System time synchronized with ntp.server.local",
    "Temporary network outage resolved on interface eth0"
    ]

    i = 1
    while i <= 5:
        z = 1
        file_id = random.randrange(1,500)
        while z <= 100:
            listy = []
            x = random.randrange(1,6000)
            y = random.randrange(1,6000)
            for option in (hostnames, systems, authentication, networking, files, jobs, security, levels, oses, messages):
                pick = random.choice(option)
                listy.append(pick)
            with open(f"system_log_{datetime.now().strftime('%Y-%m-%d')}_{file_id}_{i}.txt", "a") as f:
                f.write(f"{datetime.now()} {listy[0]} {listy[1]}[{x}]: {listy[7]}: {listy[9]} (event_id={y})\n")         
            z += 1
        i += 1

def main():
    startup()
    path_verification()
    creation()
    
if __name__ == "__main__":
    main()

