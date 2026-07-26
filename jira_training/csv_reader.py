import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_FILE = PROJECT_ROOT / "data" / "employees.csv"


def read_employees():
    employees = []
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees


if __name__ == "__main__":
    employees = read_employees()
    for employee in employees:
        print(employee)
