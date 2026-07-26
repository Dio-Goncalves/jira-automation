from jira_training.csv_reader import read_employees
from jira_training.onboarding_service import create_employee_onboarding

# This run the function that reads the CSV file and store all the values it finds in the 'employees' variable
employees = read_employees()

# Runs a loop where the imported 'create_employee_onboarding' script is executed for every employee value stored in the previously created 'employees' variable. This function then prints the responses for each onboarding request created
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
