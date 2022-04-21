# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json

import requests
import os
import json

print("Lesson 1")

user = 'Dainera'

token = os.environ.get("GITHUB_TOKEN")

uri = f'https://api.github.com/users/{user}/repos'

response = requests.get(uri, auth=(user, token))

print(response)

public_repo = []
for repo in response.json():
    if not repo['private']:
        public_repo.append(repo['html_url'])

print(public_repo)

with open('user_repos.json', 'w') as f:
    json.dump(public_repo, f)
