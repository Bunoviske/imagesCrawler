# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import cv2
import os
import dhash
from PIL import Image

"""
pip install dhash imutils
"""


from collections import OrderedDict

def my_dhash(image, hashSize=8):
	# convert the image to grayscale and resize the grayscale image,
	# adding a single column (width) so we can compute the horizontal
	# gradient
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	resized = cv2.resize(gray, (hashSize + 1, hashSize))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash and return it
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-r", "--remove", type=int, default=0,
	help="whether or not duplicates should be removed (i.e., dry run). Set 1 to activate this feature.")
ap.add_argument("-ra", "--removeall", type=int, default=0,
	help="whether or not all images that have duplicates, including original images, should be removed. Set 1 to activate this feature.")
args = vars(ap.parse_args())



# grab the paths to all images in our input dataset directory and
# then initialize our hashes dictionary
imagePaths = list(paths.list_images(args["dataset"]))
print(f"[INFO] computing image hashes... Found {len(imagePaths)} images")
hashes = {}
# loop over our image paths
cont = 0
for imagePath in imagePaths:
	# load the input image and compute the hash
	# image = cv2.imread(imagePath)
	# h = my_dhash(image)

	image = Image.open(imagePath)
	h = dhash.dhash_int(image, size=8)

	# grab all image paths with that hash, add the current image
	# path to it, and store the list back in the hashes dictionary
	p = hashes.get(h, [])
	p.append(imagePath)
	hashes[h] = p

##### check hamming distance between hashes
threshold = 10
for key in list(hashes):
	for otherKey in list(hashes):
		if otherKey != key:
			diff = dhash.get_num_bits_different(otherKey, key)
			if diff <= threshold:
				#print(diff)
				try:
					hashes[key] = hashes[key] + hashes[otherKey]
					hashes.pop(otherKey, None)
				except:
					continue

# loop over the image hashes
for (h, hashedPaths) in hashes.items():
	# check to see if there is more than one image with the same hash
	if len(hashedPaths) > 1:
		# check to see if this is a dry run
        # otherwise, we'll be removing the duplicate images
		if args["remove"] == 1:
			# loop over all image paths with the same hash *except*
			# for the first image in the list (since we want to keep
			# one, and only one, of the duplicate images)
			cont = cont + len(hashedPaths) - 1
			for p in hashedPaths[1:]:
				os.remove(p)

		elif args["removeall"] == 1:	
			cont = cont + len(hashedPaths) - 1
			for p in hashedPaths:
				os.remove(p)	

		else:
			# initialize a montage to store all images with the same
			# hash
			montage = None
			# loop over all image paths with the same hash
			for p in hashedPaths:
				# load the input image and resize it to a fixed width
				# and heightG
				image = cv2.imread(p)
				image = cv2.resize(image, (150, 150))
				# if our montage is None, initialize it
				if montage is None:
					montage = image
				# otherwise, horizontally stack the images
				else:
					montage = np.hstack([montage, image])

			cont = cont + len(hashedPaths) - 1

			# show the montage for the hash
			# print("[INFO] hash: {}".format(h))
			# cv2.imshow("Montage", montage)
			# cv2.waitKey(0)

print(f"Duplicates found {cont}")