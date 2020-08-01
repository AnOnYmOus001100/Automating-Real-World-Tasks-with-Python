#!/usr/bin/env python3

import os
import sys
from PIL import Image

user = os.getenv('USER')   # fetch username from environment variable
image_dir = '/home/{}/supplier-data/images/'.format(user) # image location
# iterating through images
for image in os.listdir(image_dir):
	if not image.startswith('.') and 'tiff' in image:
	image_path = image_dir + image
	path = os.path.splitext(image_path)[0]
	img = Image.open(image_path)
	new_path = '{}.jpeg'.format(path)
	# converting to RGB and resizing
	img.convert('RGB').resize((600,400)).save(new_path, "JPEG")
