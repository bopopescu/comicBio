import requests

#name = "green arrow"   #raw_input("Enter your favourite comic character name:\n")

payload = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json",
	'limit': 1
	#'filter': "name:" + name
}

r = requests.get("http://www.comicvine.com/api/characters", params=payload)
characters = r.json()

payload = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json",
}

r = requests.get(characters['results'][0]['api_detail_url'], params=payload)
character = r.json()

print character['results']['powers']
