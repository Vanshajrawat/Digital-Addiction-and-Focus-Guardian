import psutil
import time
import sqlite3
from datetime import datetime

DB = "guardian.db"
LOG_FILE = "app_violations.log"

def get_blocked_apps():
    with sqlite3.connect(DB) as conn:
        rows = conn.execute("SELECT app_name FROM app_blocks").fetchall()
    return [row[0].lower() for row in rows]

def log_violation(app):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - Blocked app attempt: {app}\n")

def block_apps():
    print("[+] App blocker running...")
    while True:
        blocked_apps = get_blocked_apps()

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() in blocked_apps:
                    psutil.Process(proc.info['pid']).terminate()
                    log_violation(proc.info['name'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        time.sleep(2)

if __name__ == "__main__":
    block_apps()
