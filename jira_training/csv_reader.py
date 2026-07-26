import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

CSV_FILE = BASE_DIR / "data" / "employees.csv"


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
