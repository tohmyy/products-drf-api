
import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title" : "Snowboard",
    "price": 70,
}

get_response = requests.delete(endpoint, json=data)

print(get_response.json())