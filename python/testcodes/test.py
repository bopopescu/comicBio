from urllib2 import Request, urlopen, URLError
from json import load
from pprint import pprint

try:
	response = urlopen("http://www.comicvine.com/api/characters?api_key=9b477c6dec985e48795c42203d8fdb92fa93a2c1&limit=1&format=json")
	characters = load(response)
	pprint(characters['results'][0]['aliases'])

except URLError, e:
	print "ERROR, it is!! Got an error code:", e

