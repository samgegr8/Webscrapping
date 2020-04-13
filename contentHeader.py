import requests


def print_the_response(json):
    for key, value in json.items():
        print(f"{key} {value}")


url = "https://api.github.com"
response = requests.get(url)
print(response.json())

print("Printing in a more formatted way")

json_response = response.json()
print_the_response(json_response)

print(f"Email URL :: {json_response['emails_url']}")
