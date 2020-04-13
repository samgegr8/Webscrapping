import requests
from requests.exceptions import HTTPError

for url in ["https://api.github.com", "https://api.github.com/invalid"]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as httperror:
        print(f"HTTP Error Occured:{httperror}")
    except Exception as err:
        print(f"Other Errors:{err}")
    else:
        print("Success")
