import requests
from requests.auth import HTTPBasicAuth

from config import *

url = f"{JIRA_URL}/rest/api/3/issue"

payload = {
    "fields": {
        "project": {
            "key": PROJECT_KEY
        }
    }
}
