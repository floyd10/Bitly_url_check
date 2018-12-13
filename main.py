import bitly_api

BITLY_ACCESS_TOKEN = 'e3f866bffb9af54132642b96a67353cc4f6fc123'
#e3f866bffb9af54132642b96a67353cc4f6fc123

bitly = bitly_api.bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
longurl = 'http://mail.ru/'
response = bitly.shorten(uri=longurl)
shortUrl = response['url']
cliks = bitly.link_clicks(link=shortUrl)
#response = input("Enter a url: ")


print (response['url'])



print([cliks])
print((bitly.link_countries(link=shortUrl)))
