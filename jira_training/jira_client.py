# Centralized client for HTTP communication. Stores authentication and endpoint information.

import requests
from requests.auth import HTTPBasicAuth

from jira_training.config import (
    JIRA_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN
)

# Authentication with imported data
auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

# Required headers for GET and POST requests
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Function that builds the payload to create request
def create_requests(service_desk_id, request_type_id, fields):
    url = f"{JIRA_URL}/rest/servicedeskapi/request"

    payload = {
        "serviceDeskId": str(service_desk_id),
        "requestTypeId": str(request_type_id),
        "requestFieldValues": fields
    }

    from pprint import pprint
    print("Payload being sent:")
    pprint(payload)
    print

    response = requests.post(
        url,
        json=payload,
        auth=auth,
        headers=headers
    )

    return response

# Private helper function that performs GET requests to Jira
def _get(endpoint):
    url = f"{JIRA_URL}{endpoint}"

    return requests.get(
        url,
        auth=auth,
        headers=headers
    )


# Function to retrieve every service desk available in Jira Service Management
def get_service_desks():
    return _get("/rest/servicedeskapi/servicedesk")


# This function gets request types for different service desk IDs without having to hardcode the endpoint URL
def get_request_types(service_desk_id):
    return _get(
        f"/rest/servicedeskapi/servicedesk/{service_desk_id}/requesttype"
    )


# Search Jira users
def search_users(query):
    return _get(f"/rest/api/3/user/search?query={query}")

# Search users and transform data into a python list
def get_user_account_id(name):
    response = search_users(name)

    users = response.json()

    if not users:
        raise ValueError(f"No Jira user found matching '{name}'")

    return users[0]["accountId"]
