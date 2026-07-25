from csv_reader import read_employees
from create_onboarding import create_employee_onboarding

employees = read_employees()

for employee in employees:
    response = create_employee_onboarding(employee)
    print(response.status_code)
