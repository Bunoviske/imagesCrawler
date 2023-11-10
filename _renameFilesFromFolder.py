
######### rename files from folder ############

import os
import pathlib
import argparse
from imutils import paths

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, required=True,
	help="path to input dataset")
ap.add_argument("-o", "--offset", type=int, required=True,
	help="offset to represent first image name. Here should be only int")
ap.add_argument("-r", "--recursion", type=int, default=0,
	help="whether or not to search for images in subfolders recursively")
args = vars(ap.parse_args())

path = args["dataset"]
offset = args["offset"]

if args["recursion"] == 0:
    files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
else:
    files = list(paths.list_images(path))

for index, file in enumerate(files):
    folder = pathlib.Path(file).parent
    extension = pathlib.Path(file).suffix
    os.rename(file, os.path.join(folder, ''.join([str(index + offset), extension])))
        