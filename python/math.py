import re
import json

imageData = open("imageData.txt", "r")

searchObj = []

ratios = [] 

for i,size in enumerate(imageData):
	searchObj.append(re.findall(r'\d+', size, re.M|re.I))
	# searchObj.append(re.findall(r'[0-9][0-9]*', size, re.M|re.I))
	
	ratios.append(float(searchObj[i][1])/float(searchObj[i][0]))


listRatios = [0]*30
for number in range(len(ratios)):
	# listRatios[int((ratios[number] - 0.5) * 10)].append(ratios[number])
	listRatios[int((ratios[number] - 0.5) * 10)] += 1

object = {}
object["val"] = listRatios
json_data = json.dumps(object)

sum = 0
count = 0
for i in range(len(ratios)):
	if ratios[i] > 0.5 and ratios[i] < 2.2:
		sum += ratios[i]
		count += 1

print sum/count
 