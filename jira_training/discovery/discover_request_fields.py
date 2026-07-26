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

print(f"Status: {response.status_code}")

data = response.json()

for field in data["requestTypeFields"]:
    print(f"Name: {field['name']}")
    print(f"ID: {field['fieldId']}")
    print(field["jiraSchema"])
    print(field["validValues"])
    print(f"Required: {field['required']}")
    print("-" * 40)

for field in data["requestTypeFields"]:
    if field["fieldId"] == "customfield_10132":
        pprint(field)
