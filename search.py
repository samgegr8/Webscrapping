import requests

# Search Github Repositories

response = requests.get(
    "https://api.github.com/search/repositories", params={"q": "schedule+user:dbader"},
)

# Inpecting source elements
json_response = response.json()
repository = json_response["items"][0]

print(f'Repository Name :: {repository["name"]}')
print(f'Repository Description :: {repository["description"]}')
