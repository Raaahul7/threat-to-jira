def map_severity_to_priority(severity):
    return {
        "High": "Highest",
        "Medium": "High",
        "Low": "Medium"
    }.get(severity, "Low")


def map_threat_to_jira(threat, project_key):
    mitigations = "\n".join(f"- {m}" for m in threat["mitigations"])

    description = f"""
Threat ID: {threat['id']}
Category: {threat['category']}
CVSS Rating: {threat['cvss_rating']}

Description:
{threat['description']}

Mitigations:
{mitigations}
"""

    return {
        "fields": {
            "project": {"key": project_key},
            "summary": f"{threat['id']} - {threat['title']}",
            "description": description,
            "issuetype": {"name": "Bug"},
            "priority": {"name": map_severity_to_priority(threat["severity"])}
        }
    }

