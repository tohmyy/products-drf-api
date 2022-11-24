

from unittest import result
import requests
from getpass import getpass


auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input("What's your username? \n")
password = getpass("What's your password? \n")
auth_post = requests.post(auth_endpoint, json={'username':username, 'password': password})

print(auth_post.json())


if auth_post.status_code==200:
    token = auth_post.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())

#pagination
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print()
    print(results)
