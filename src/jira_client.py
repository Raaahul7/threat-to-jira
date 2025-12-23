import requests
from requests.auth import HTTPBasicAuth
from config import Config

class JiraClient:
    def __init__(self):
        self.base_url = Config.JIRA_BASE_URL
        self.auth = HTTPBasicAuth(Config.JIRA_EMAIL, Config.JIRA_API_TOKEN)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def search_issue(self, threat_id):
        jql = f'summary ~ "{threat_id}"'
        url = f"{self.base_url}/rest/api/3/search"
        response = requests.get(
            url, headers=self.headers, auth=self.auth, params={"jql": jql}
        )
        response.raise_for_status()
        return response.json()["total"] > 0

    def create_issue(self, payload):
        url = f"{self.base_url}/rest/api/3/issue"
        response = requests.post(
            url, headers=self.headers, auth=self.auth, json=payload
        )
        response.raise_for_status()
        return response.json()

