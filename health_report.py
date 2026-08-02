#!/usr/bin/env python3
import csv

CSV_FILE = "/home/trung/Projects/devops-journey/week1/health.csv"

def report():
    cpu_list = []
    ram_list = []

    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cpu_list.append(float(row['cpu_percent']))
            ram_list.append(float(row['ram_percent']))

    if not cpu_list:
        print("No data")
        return

    cpu_avg = sum(cpu_list) / len(cpu_list)
    cpu_max = max(cpu_list) or 0
    ram_avg = sum(ram_list) / len(ram_list)

    print("=" * 40)
    print("SERVER HEALTH REPORT")
    print("=" * 40)
    print(f"Count Number: {len(cpu_list)}")
    print(f"CPU average: {cpu_avg:.1f}%")
    print(f"CPU maximum: {cpu_max:.1f}%")
    print(f"RAM average: {ram_avg:.1f}%")

    if cpu_max > 80:
        print("Warning: CPU overate 80%!")
    else:
        print("CPU stable")
    print("=" * 40)

if __name__ == '__main__':
    report()
