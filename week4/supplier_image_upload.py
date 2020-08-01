#!/usr/bin/env python3

import requests
import os

# image upload url
url = "http://localhost/upload/"
# fetch user
user = os.getenv('USER')
# image directory
img_dir = '/home/{}/supplier-data/images/'.format(user)
# list all files in img_dir
img_files = os.listdir(img_dir)
# iterating through images
for img in img_files:
	# only checking for files with jpeg extension and ignore hidden files
	if not img.startswith('.') and 'jpeg' in img:
		# create absolute path
		img_path = img_dir + img
		# upload image
		with open(img_path, 'rb') as img_file:
			r = requests.post(url, files={'file': img_file})
