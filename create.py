#!/usr/bin/env python

import os
import sys
import random
import shutil
from images2gif import writeGif

try:
	import PIL
	import PIL.GifImagePlugin
except ImportError:
	sys.exit("Module PIL missing.\nAborting.")

try:
	import Image
except ImportError:
	sys.exit("Module PIL missing.\nAborting.")

def makedir(folder):
	try:
		if os.path.exists(folder):
			shutil.rmtree(folder)
		os.makedirs(folder)
		os.chdir(folder)
	except OSError as e:
		sys.exit(3)

def create(num_images, size, img_size):
	pos = 1
	for _ in range(num_images):
		im = Image.new("RGB", (img_size,img_size))
		z = range(256)
		array = []
		for _ in range(size):
			values = [[(
				# warm colors? range(220,250)
				random.choice(z),
				random.choice(z),
				random.choice(z))]*size for _ in range(size)]
			for _ in range(size):
				array += values

		im.putdata([elem for subl in array for elem in subl])
		im.save(str(pos) + ".png")
		array = []
		pos += 1

def transform(num_images, output_file, size, img_size):
    makedir(".images")
    create(num_images, size, img_size)
    images = [Image.open(fn) for fn in os.listdir(".")]
    os.chdir("..")
    writeGif(output_file, images, duration=0.1, loops=0, dither=0)
    shutil.rmtree(".images")   
	
if __name__ == '__main__':
    size=25
    img_size=size*size
    print ("Creating gif...")
    transform(20, "animation.gif",size,img_size)
