import requests

endpoint = "http://localhost:8000/api/products/"
headers = {'Authorization': 'Token b38c5251c72fb89db174743adbfd116e0349fa0d'}

# so create api will now require an authorization token to work  

data = {
    "title": "Bicycle",
    "price": 100,
}

post_response = requests.post(endpoint, json=data, headers =headers)
print(post_response.json())