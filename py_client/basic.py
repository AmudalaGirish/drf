import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query":"Hello world"}) # Http Request

print(get_response.json())
print(get_response.status_code)
# print(get_response.text)
