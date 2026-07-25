from jira_client import create_requests

SERVICE_DESK_ID = 1
ONBOARDING_REQUEST_TYPE = 8


def create_employee_onboarding(employee):
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
    }

    response = create_requests(
        SERVICE_DESK_ID,
        ONBOARDING_REQUEST_TYPE,
        fields,
    )

    return response
