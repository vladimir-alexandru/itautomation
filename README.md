# Repo: /vladimir-alexandru/itautomation  

**Description:**  
Python and IT automation scripts for system administration and cybersecurity tasks.

---

### Script: `folder_summary_v1.py`  
**Purpose:**  
Summarizes the contents of a specified folder, counting files and directories.  

**Key Features:**  
- Validates user input and handles invalid paths gracefully.  
- Displays file and directory counts for the target folder.  
- Optionally exports results with timestamps to a text report.  

**Usage:**  
Run the script, enter a folder path, confirm it, and choose whether to save the summary.  

**Tech:**  
Uses built-in Python modules (`os`, `sys`, `platform`, `datetime`).  

---

### Script: 'log_creator.py'

**Purpose:**
Creates practice log files on the local machine for testing and automation exercises.

**Key Features:**
- Displays basic system info (OS, version, user).
- Prompts the user to scan a drive to check available space before creating files.
- Uses retry logic for invalid partition input.
- Gracefully exits if the user declines or exceeds allowed attempts.

**Usage:**
Run the script and follow prompts to select a partition. The program reports disk usage and exits safely after validation.

**Tech:**
Uses built-in Python modules (`os`, `platform`, `getpass`) and `psutil` for disk information.

---

### Script: `log_archiver.py` COMING SOON!

**Purpose:**
Automates the management of system log files by moving, renaming, and cleaning up old logs in designated directories.

**Key Features:**
- Scans a source folder for .log files.
- Moves and renames logs with the current date appended.
- Deletes archived logs older than 30 days.
- Handles missing directories or permission errors gracefully.
- Prints a clear summary of actions taken.

**Usage:**
Run the script manually or schedule it with cron (Linux) or Task Scheduler (Windows). It will automatically organize logs from the configured source to the archive folder and clean up old files.

**Tech:**
Uses built-in Python modules (`os`, `shutil`, `glob`, `datetime`, `logging`).

---

### Script: `logon_checker.py` COMING SOON!