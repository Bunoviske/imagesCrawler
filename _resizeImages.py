from fastai.basics import *
from fastai.callback.all import *
from fastai.vision.all import *
from PIL import Image


def resizeBasedOnWidth(file):
    basewidth = 1000
    img = Image.open(file)
    wpercent = (basewidth/float(img.size[0]))
    if wpercent < 1:
        print("Resize because file has big width:", file)
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(file)

def resizeBasedOnHeight(file):
    baseHeight = 1000
    img = Image.open(file)
    hpercent = (baseHeight/float(img.size[1]))
    if hpercent < 1:
        print("Resize because file has big height:", file)
        wsize = int((float(img.size[0])*float(hpercent)))
        img = img.resize((wsize,baseHeight), Image.ANTIALIAS)
        img.save(file)


path = './database'
fnames = get_image_files(path)

print("Resizing big images...")
for file in fnames:
    resizeBasedOnWidth(file)
    resizeBasedOnHeight(file)



