import requests
from requests.auth import HTTPBasicAuth

from config import(
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
	data = response.json()
	print(f"Connected as: {data['displayName']}")
	print(f"Account ID: {data['accountId']}")
else:
	print(response.text)
