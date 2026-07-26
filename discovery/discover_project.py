import requests
from requests.auth import HTTPBasicAuth

from config import (
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
print("Project Information")
print("-------------------")
print(f"Name: {project['name']}")
print(f"Key: {project['key']}")
print(f"Project ID: {project['id']}")
print(f"Project Type: {project['projectTypeKey']}")
