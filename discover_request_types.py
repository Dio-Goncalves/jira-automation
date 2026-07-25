from pprint import pprint
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

print(type(project))
print(project.keys())
pprint(project)
