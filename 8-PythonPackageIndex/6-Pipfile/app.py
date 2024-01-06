import requests

response = requests.get("http://google.com")
print(response)


# to have the exact version of packages, pipfile.lock should be used then pipfile should be ignored by the command: pipenv install --ignore-pipfile
