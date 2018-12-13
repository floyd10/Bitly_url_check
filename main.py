import bitly_api
import requests
import json



#class bitly():

url = 'http://mail.ru'
BITLY_ACCESS_TOKEN = 'e3f866bffb9af54132642b96a67353cc4f6fc123'

def url_shortner(url, BITLY_ACCESS_TOKEN):

  params = {
     'longUrl': url,
     'access_token': BITLY_ACCESS_TOKEN
  }
  endpoint = 'https://api-ssl.bitly.com/v3/shorten'
  response = (requests.get(endpoint, params=params)).content
  #print(response)
  data = json.loads(response)['data']
  tag_url = data.get('url')
  tag_hash = data.get('hash')
  return tag_url, tag_hash


def url_stat(url_hash,url_short,BITLY_ACCESS_TOKEN):

    params = {
        'hash': '',
        'shortUrl': url_short,
        'access_token': BITLY_ACCESS_TOKEN
    }
    endpoint = 'https://api-ssl.bitly.com/v3/clicks'
    response = (requests.get(endpoint, params=params)).content
    #print(response)
    data = json.loads(response)['data']
    #print(data)
    clicks_data = (data.get('clicks')[0])
    print('Информация по сокращенной ссылке :' , clicks_data)
    user_clicks = clicks_data['user_clicks']
    print('Количество переходов по сокращенной ссылке: ', user_clicks)
    return user_clicks

url_short = url_shortner(url,BITLY_ACCESS_TOKEN)[0]
url_hash = url_shortner(url,BITLY_ACCESS_TOKEN)[1]

print('Сокращенная ссылка: ', url_short)

url_stat(url_hash,url_short,BITLY_ACCESS_TOKEN)
