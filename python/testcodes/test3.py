import requests

payload = {
	'apikey': "28d755dfe3546ee7aaefe24243fd27ef",
	'format': "json",
	'limit': "5",
	'ts': "1",
	'hash': "103d2145e9b5021f5b9e3397f55a5c1ec5118311128d755dfe3546ee7aaefe24243fd27ef"
}

r = requests.get("http://gateway.marvel.com/v1/public/characters", params=payload)
characters = r.json()

print characters