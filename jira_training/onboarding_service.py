from jira_training.jira_client import (
    create_requests,
    get_user_account_id,
)

SERVICE_DESK_ID = 1
ONBOARDING_REQUEST_TYPE = 8

# Since the Departments field is a select list, below we have to describe all the valid options and store it in a variable. Below we'll mention this in 'fields'.

DEPARTMENTS = {
    "Customer Service": "10073",
    "Engineering": "10074",
    "Facilities": "10075",
    "Finance": "10076",
    "Human Resources": "10077",
    "Information Technology": "10078",
    "Legal": "10079",
    "Marketing": "10080",
    "Procurement": "10081",
    "Sales": "10082",
    "Supply Chain": "10083",
    "Other": "10084",
}


def create_employee_onboarding(employee):

    manager_account_id = get_user_account_id(
        employee["manager"]
    )

# Making use of the imported 'get_user_account_id' function from 'jira_client.py' to create a new 'manager_account_id' function that'll find the id of the manager name fed by the CSV file.    
    
    summary = (
        f"New employee onboarding - "
        f"{employee['first_name']} {employee['last_name']}"
    )

    description = (
        f"Employee: {employee['first_name']} {employee['last_name']}\n"
        f"Email: {employee['email']}\n"
        f"Department: {employee['department']}\n"
        f"Manager: {employee['manager']}"
    )

# Since Department is a select list and not a text field (option and not a string) we have to send an option object. Hence why its written for the custom field related to it.
# The formatting is also changed for the manager custom field. This is because its an array type field. Here we make use of the 'manager_account_id' function to solve the manager's name.
    
    fields = {
        "summary": summary,
        "description": description,
        "customfield_10118": employee["first_name"],
        "customfield_10120": employee["last_name"],
        "customfield_10123": employee["email"],
        "customfield_10131": {
            "id": DEPARTMENTS[employee["department"]]
        },
        "customfield_10132": [
            {
                "accountId": manager_account_id
            }
        ]
    }

    response = create_requests(
        SERVICE_DESK_ID,
        ONBOARDING_REQUEST_TYPE,
        fields,
    )

    return response
