from operator import ge
from django.http import HttpResponsePermanentRedirect
import requests


# endpoint= "https://httpbin.org/status/200"
# endpoint= "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"



get_response = requests.post(endpoint, json = {"title": "Arcade Game" } ) #this will get data (an api method of getting data)
               #but not rest api just (library api)
# print(get_response.text)
# print(get_response.headers)
# print(get_response.text) #prints raw (body) html code
#REST api is a web


print(get_response.json())
# print(get_response.status_code)