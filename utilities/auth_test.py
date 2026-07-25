import requests
from requests.auth import HTTPBasicAuth

from config import (
    JIRA_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN,
)

url = f"{JIRA_URL}/rest/api/3/myself"

response = requests.get(
    url,
    auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
    headers={
        "Accept": "application/json"
    }
)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    me = response.json()

    print()
    print("Authentication Successful!")
    print("--------------------------")
    print(f"Name: {me['displayName']}")
    print(f"Account ID: {me['accountId']}")
    print(f"Email: {me.get('emailAddress', 'Hidden by Atlassian')}")
else:
    print(response.text)
