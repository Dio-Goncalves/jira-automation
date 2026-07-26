# Importing necesary libraries to make this script work: python's built-in CSV module and pathlib to enable directory referencing
import csv
from pathlib import Path

# Here we indicate where the project root is, using this script's location as reference. Translated to linux terms: "Path(__file__).resolve()" = "pwd" and ".parent.parent" = "cd .." (x2). We are basically saying that the root directory of this project is 2 levels above.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Here we create the CSV_FILE variable, storing the location of our CSV file. For the location we use the previously created PROJECT_ROOT variable as reference.
CSV_FILE = PROJECT_ROOT / "data" / "employees.csv"

# This function reads the CSV file and returns the employees as a dictionary. It creates an empty list and then populates it with the contents of the file, nicely formatted with DictReader.
def read_employees():
    employees = []
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

# Module included for test purposes. This will allow to print the output of this code if you execute this file directly, useful for troubleshooting. If you merely import this file, the functions will be available but the output won't be printed.
if __name__ == "__main__":
    employees = read_employees()
    for employee in employees:
        print(employee)
