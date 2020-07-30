#!/usr/bin/env python3

import os
import requests

# data location
data = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

# list of all files in /data/feedback
files = os.listdir(data)

# iterating through files
for f in files:
	# counter set to 0
	count = 0
	# intialising blank dictionary
	dic = {}
	# opening file
	with open(data + f) as f1:
		for line in f1:
			value = line.strip()
			dic[keys[count]] = value
			count += 1
	print (dic)
	
	# posting the data to the website
	response = requests.post("http://<corpweb-external-IP address>/feedback/",json=dic)

print (response.request.body)
print (response.status_code)
