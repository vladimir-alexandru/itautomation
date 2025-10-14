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
1. Scan a partition to view available space (Optional).
2. Choose where to create your test logs.
3. Watch as the program builds a folder of randomly generated log files.

You can repeat file generation or quit safely at any prompt.

**Tech:**
Built with standard Python libraries (`os`, `sys`, `time`, `random`, `getpass`, `platform`, `datetime`) and `psutil` for drive statistics.

---

### Script: `password_auditor_v1.0.py` (Windows & Linux)

**Purpose:** Evaluates password strength based on core security criteria and provides instant feedback in a command-line interface.

**Key Features:**
- Interactive startup prompt with safe exit and countdown.
- Secure password input (hidden using getpass).
- Checks for uppercase, lowercase, digits, special characters, and minimum length (12).
- Displays individual pass/fail messages for each requirement.
- Calculates overall password strength: Weak, Strong, or Excellent.
- Ability to test multiple passwords in a single session. (Optional)

**Usage:**
Run the script, confirm when prompted, and enter a password to audit. 
After evaluation, you can choose to test another password or exit safely.

**Tech:**
Built entirely with standard Python libraries (`time`, `sys`, `getpass`).

---

### Script: `hash_guard_v1.0.py` (Windows & Linux)

**Purpose:** Scans a chosen folder, computes SHA-256 hashes for all files, and outputs a report for future integrity verification.

**Key Features:**
- Interactive startup with OS/user info and safe exit option (q).
- Validates path input (Current version blocks access to root/system directories for safety).
- Reads all files in binary mode and generates SHA-256 hashes.
- Saves results in a timestamped hash_report_YYYY-MM-DD_HHh-MMm-SSs.txt.
- Displays total files processed and total runtime.
- Continuous session with the ability to rerun multiple scans.

**Usage:**
Run the script, enter a valid folder path, and wait while it hashes each file.
After completion, view or compare the generated report to check for tampering or data integrity changes.

**Tech:**
Built entirely with standard Python libraries (`os`, `sys`, `hashlib`, `time`, `platform`, `getpass`, `datetime`).

---

### Script: `log_auditor_v1.0.py` (Windows & Linux)

**Purpose:** Scans and filters log files by severity level, helping users quickly identify and extract relevant log entries.

**Key Features:**
- Interactive command-line interface with safe quit options.
- Validates folder paths before parsing.
- Supports multiple log severity levels: INFO, WARN, ERROR, DEBUG, NOTICE, and CRITICAL.
- Reads all files in a selected folder (skipping subfolders).
- Collects and displays lines matching the chosen severity level.
- Export results to a timestamped text report (optional).

**Usage:**
Run the script, provide the folder path containing your logs, and select a log severity level to audit.
After processing, you can export the filtered results as a report or check another folder.
You can try it out on the sample logs provided in the folder to see how it works.

**Tech:**
Developed using standard Python libraries (`os`, `sys`, `datetime`).