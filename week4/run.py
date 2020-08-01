#!/usr/bin/env python3

import os
import requests
import json

def catalog_data(url,description_dir):
	# returns list of dictonaries with all details
	fruit = {}
	for item in os.listdir(description_dir):
		fruit.clear()
		filename = os.path.join(description_dir,item)
		with open(filename) as f:
			line = f.readlines()
			description = ""
			for i in range(2,len(line)):
				description = description + line[i].strip('\n').replace(u'\xa0',u'')
				fruit["description"] = description
				fruit["weight"] = int(line[1].strip('\n').strip('lbs'))
				fruit["name"] = line[0].strip('\n')
				fruit["image_name"] = (item.strip('.txt'))+'.jpeg'
				print (fruit)
				if url != "":
					response = requests.post(url, json=fruit)
					print (response.request.url)
					print (response.status_code)
	return 0

if __name__ == '__main__':
	url = 'http://localhost/fruits/'
	user = os.getenv('USER')
	description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
	catalog_data(url,description_directory)
