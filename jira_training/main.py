from jira_training.csv_reader import read_employees
from jira_training.onboarding_service import create_employee_onboarding

employees = read_employees()

for employee in employees:
    response = create_employee_onboarding(employee)
    print(response.status_code)

    if response.status_code == 201:
        data = response.json()
        print(
            f"Created request {data['issueKey']}"
            f" for {employee['first_name']} {employee['last_name']}"
        )
    else:
        print(response.status_code)
        print(response.text)
