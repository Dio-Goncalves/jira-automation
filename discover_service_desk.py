import requests
from requests.auth import HTTPBasicAuth

from config import *

url = f"{JIRA_URL}/rest/servicedeskapi/servicedesk"

response = requests.get(
    url,
    auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
    headers={
        "Accept": "application/json"
    }
)

print(f"Status: {response.status_code}")


project = response.json()

for service_desk in project["values"]:
    print(f"Service Desk: {service_desk['projectName']}")
    print(f"Service Desk ID: {service_desk['id']}")
    print(f"Project Key: {service_desk['projectKey']}")
    print()
    print("-" * 30)
    print()
