# Repo: /vladimir-alexandru/itautomation  

**Description:**  
Python and IT automation scripts for system administration and cybersecurity tasks.

---

### Script: `folder_summary_v1.0.py`  

**Purpose:** Summarizes the contents of a specified folder, counting files and directories.  

**Key Features:**  
- Validates user input and handles invalid paths gracefully.  
- Displays file and directory counts for the target folder.  
- Optionally exports results with timestamps to a text report.  

**Usage:**  
Run the script, enter a folder path, confirm it, and choose whether to save the summary.  

**Tech:**  
Uses built-in Python modules (`os`, `sys`, `platform`, `datetime`).  

---

### Script: `log_creator_Win_v1.0.py` (Windows-only Version)

**Purpose:** Generates practice log files on your local machine for testing, parsing, or automation exercises

**Key Features:**
- Shows system details (OS, version, username, date).
- Optionally scans a selected drive to display free and used disk space.
- Creates a new folder and generates multiple randomized log files (10 by default, 100 lines each).
- Includes input validation, retry limits, and graceful exit options (q to quit anytime).
- Provides countdown messages and clear on-screen feedback during each stage.

**Usage:**
Follow the interactive prompts to:
1. Scan a partition to view available space. (Optional)
2. Choose where to create your test logs.
3. Watch as the program builds a folder of randomly generated log files.

You can repeat file generation or quit safely at any prompt.

**Tech:**
Built with standard Python libraries (`os`, `sys`, `time`, `random`, `getpass`, `platform`, `datetime`) and `psutil` for drive statistics.

---

### Script: `password_auditor_v1.0.py` (Work in progress)

**Purpose:** Audits user-entered passwords for basic strength indicators and provides simple feedback.

**Key Features:**
- Interactive CLI with user confirmation and countdown exit.

**Usage:**
Run the script, confirm you want to proceed, and enter a password when prompted.

**Tech:**
Uses built-in Python modules (`time`, `sys`, `getpass`).