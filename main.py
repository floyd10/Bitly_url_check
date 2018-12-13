import bitly_api
import requests
import json


BITLY_ACCESS_TOKEN = 'e3f866bffb9af54132642b96a67353cc4f6fc123'

params = {
    'longUrl': 'http://mail.ru',
    'access_token': BITLY_ACCESS_TOKEN
}
endpoint = 'https://api-ssl.bitly.com/v3/shorten'
response = (requests.get(endpoint, params=params)).content
#print(response)

data = json.loads(response)['data']
tag = data.get('url')

print(tag)