import numpy as np
from PIL import Image
import matplotlib
import os

#read all images'name
images=os.listdir('./images/')

#conver all images into gray
for image in images:
	image_file = Image.open('./images/'+image) # open colour image
	image_file = image_file.convert('1') # convert image to black and white
	image_file.save('./gray_images/'+image)
print(images)

#255 to 1 0 to 0