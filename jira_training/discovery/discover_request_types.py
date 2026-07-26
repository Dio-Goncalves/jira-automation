from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth

from jira_training.config import *

url = f"{JIRA_URL}/rest/servicedeskapi/servicedesk/1/requesttype"

response = requests.get(
    url,
    auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
    headers={
        "Accept": "application/json"
    }
)

print(f"Status: {response.status_code}")


project = response.json()

for request_type in project["values"]:
    print(f"Request Type id: {request_type['id']}")
    print(f"Request Type name: {request_type['name']}")
    print(f"Request Type description: {request_type['description']}")
    print()
    print("-" * 30)
    print()
