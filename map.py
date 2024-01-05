envs = {
    "NEW_RELIC_AGENT_ENABLED": "true",
    "NEW_RELIC_APP_ID": "1491436248",
    "NEW_RELIC_APP_NAME": "calls-router-web",
    "NEW_RELIC_LICENSE_KEY": "123"
}

for key in envs:
    print(key, envs[key])
