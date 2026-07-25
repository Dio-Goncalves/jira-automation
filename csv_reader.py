import csv


def read_employees(filename):
    employees = []
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employees.append(row)
    return employees


employees = read_employees("employees.csv")

for employee in employees:
    print(employee["first_name"])
    print(employee["last_name"])
    print(employee["department"])
    print(employee["vpn"])
    print("-" * 30)
