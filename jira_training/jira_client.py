import requests
from requests.auth import HTTPBasicAuth

from config import (
    JIRA_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN
)

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def create_requests(service_desk_id, request_type_id, fields):
    url = f"{JIRA_URL}/rest/servicedeskapi/request"

    payload = {
        "serviceDeskId": str(service_desk_id),
        "requestTypeId": str(request_type_id),
        "requestFieldValues": fields
    }

    from pprint import pprint
    print("\nPayload being sent:")
    pprint(payload)
    print

    response = requests.post(
        url,
        json=payload,
        auth=auth,
        headers=headers
    )

    return response


def _get(endpoint):
    url = f"{JIRA_URL}{endpoint}"

    return requests.get(
        url,
        auth=auth,
        headers=headers
    )


def get_service_desks():
    return _get("/rest/servicedeskapi/servicedesk")


def get_request_types(service_desk_id):
    return _get(
        f"/rest/servicedeskapi/servicedesk/{service_desk_id}/requesttype"
    )


def search_users(query):
    return _get(f"/rest/api/3/user/search?query={query}")


def get_user_account_id(name):
    response = search_users(name)

    users = response.json()

    if not users:
        raise ValueError(f"No Jira user found matching '{name}'")

    return users[0]["accountId"]
