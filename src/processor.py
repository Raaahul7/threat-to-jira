from jira_client import JiraClient
from mapper import map_threat_to_jira
from config import Config

def process_threats(threats):
    jira = JiraClient()

    for threat in threats:
        if jira.search_issue(threat["id"]):
            print(f"Skipping duplicate threat {threat['id']}")
            continue

        payload = map_threat_to_jira(threat, Config.JIRA_PROJECT_KEY)
        jira.create_issue(payload)
        print(f"Created Jira ticket for {threat['id']}")

