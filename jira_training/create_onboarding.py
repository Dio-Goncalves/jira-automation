from jira_client import (
    create_requests,
    get_user_account_id,
)
from jira_training.jira_client import create_requests

SERVICE_DESK_ID = 1
ONBOARDING_REQUEST_TYPE = 8

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
