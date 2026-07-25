import requests
from requests.auth import HTTPBasicAuth

from config import *

url = f"{JIRA_URL}/rest/servicedeskapi/request"

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "serviceDeskId": "1",
    "requestTypeId": "8",
    "requestFieldValues": {
        "summary": "New employee onboarding - Diogo Gonçalves",
        "description": "Create Active Directory account, email and VPN access."
    }
}

response = requests.post(
    url,
    json=payload,
    auth=auth,
    headers=headers
)

print(response.status_code)
print(response.text)
