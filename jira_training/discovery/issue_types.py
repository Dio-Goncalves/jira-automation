import requests
from requests.auth import HTTPBasicAuth

from jira_training.config import (
    JIRA_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN,
    PROJECT_KEY
)

url = f"{JIRA_URL}/rest/api/3/project/{PROJECT_KEY}"

response = requests.get(
    url,
    auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
    headers={
        "Accept": "application/json"
    }
)

print(f"Status: {response.status_code}")

project = response.json()

print()
print("Issue Types")
print("-----------")
print()
for issue_type in project["issueTypes"]:
    print(issue_type["id"])
    print(issue_type["name"])
    print()
