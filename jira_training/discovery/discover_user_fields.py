from jira_training.jira_client import search_users
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth

from jira_training.config import (
    JIRA_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN
)

SERVICE_DESK_ID = 1
REQUEST_TYPE_ID = 8

url = (
    f"{JIRA_URL}/rest/servicedeskapi/"
    f"servicedesk/{SERVICE_DESK_ID}/"
    f"requesttype/{REQUEST_TYPE_ID}/field"
)

response = requests.get(
    url,
    auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
    headers={
        "Accept": "application/json"
    }
)

response = search_users("Diogo")

print(response.status_code)

data = response.json()
print(data)
print(type(data))
print(len(data))
print(response.url)
