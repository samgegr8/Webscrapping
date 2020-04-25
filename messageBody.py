import requests

url = "https://httpbin.org/post"

# POST Data Message Investigationnin Data JSON Format
response_data = requests.post(
    url, data={"key": "value", "brand": "Ford", "year": "2007"}
)


json_response = response_data.json()

print(f"JSON Response DATA:: {json_response}")
print(f' Content Header DATA:: {json_response["headers"]["Content-Type"]}')

# POST Data Message Investigationnin Data Tuples Format

response_tuples = requests.post(
    url, data=[("key", "value"), ("brand", "Ford"), ("year", "2007")]
)
json_response_tuples = response_tuples.json()

print(f"JSON Response Tuples :: {json_response_tuples}")
print(f' Content Header Tuples :: {json_response_tuples["headers"]["Content-Type"]}')

# POST Data Message Investigationnin JSON as parameter

response_data_json = requests.post(
    url, json={"key": "value", "brand": "Ford", "year": "2007"}
)


json_response_json = response_data_json.json()


print(f"JSON Response JSON :: {json_response_json}")
print(f' Content Header JSON:: {json_response_json["headers"]["Content-Type"]}')


print(f" Path :: {response_data_json.request.headers}")
