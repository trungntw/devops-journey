#!/usr/bin/env python3
import psutil
import datetime
import csv
import os

CSV_FILE ="/home/trung/Projects/devops-journey/week1/health.csv"

def collect():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['time', 'cpu_percent', 'ram_percent', 'disk_percent'])
        writer.writerow([now, cpu, ram, disk])
        
    print(f"[{now}] CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

if __name__ == '__main__':
    collect()
