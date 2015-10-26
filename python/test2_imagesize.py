import requests, cStringIO
from PIL import Image


payload = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json",
	'limit': 100
}

r = requests.get("http://www.comicvine.com/api/characters", params=payload)
characters = r.json()

imageUrls = []
for item in range(len(characters['results'])):
	if item not in [33,34,50,55,65,69,95,98,99]:
		imageUrls.append(characters['results'][item]['image']['super_url'])
	else:
		pass

payload1 = {
	'api_key' : "9b477c6dec985e48795c42203d8fdb92fa93a2c1",
	'format': "json"
}

images = []
for item in range(len(imageUrls)):
	r = requests.get(imageUrls[item])
	file = cStringIO.StringIO(r.content)                # This converts the response of given get-request in file format
	images.append(Image.open(file))						# which is then appended to the images list.

imageData = open("imageData.txt", "w") 
for item in range(len(images)):
	imageData.write(str(images[item].size)+"\n")

imageData.close()
print "\n----copying data to file successful!!-----\n"

