import requests

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "liane"
TOKEN = "qwrBT3784t3q"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": "graph1",
    "name": "liane",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers_config = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers_config)
print(response.text)