import requests

from requests.exceptions import Timeout

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=0.5,).json()

except Timeout:
    print("The Request Timed Out")
else:
    # Printing the one of the Key to indicate that the response is working fine
    print("The Request Didnt Timed out")
    print(f'Timeout Response :: {response["current_user_url"]}')
