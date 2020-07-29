#!/usr/bin/env python3

# importing modules
import os
import sys
# importing Image module from PIL library(currently pillow)
from PIL import Image

# image resolution set to 128 x 128 pixels
res = (128,128)

# iterating through images
for input_file in os.listdir():
	# output file
	output_file = os.path.splitext(input_file)[0]
	# trying to open image for formatting
	try:
		# opening image as img in RGB
		with Image.open(input_file).convert('RGB') as img:
			# resizing image
			img.thumbnail(res)
			# rotating image and saving the output in /opt/icons in JPEG format
			img.rotate(270).save("/opt/icons/" + output_file, "JPEG")
	# if unable to open file
	except OSError:
		pass
