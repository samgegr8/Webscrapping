import requests

url = "https://api.github.com"

response = requests.get(url)

print("Valid URL Response::", response.status_code)
url_invalid = "https://api.github.com/invalid"

response = requests.get(url_invalid)
print("Invalid URL Response::", response.status_code)

if response.status_code == 200:
    print("Success")
elif response.status_code == 404:
    print("Client Error")
