from fastai.basics import *
from fastai.callback.all import *
from fastai.vision.all import *
from PIL import Image

path = './database'
fnames = get_image_files(path)


for file in fnames:
    basewidth = 900
    img = Image.open(file)
    wpercent = (basewidth/float(img.size[0]))
    if wpercent <= 1:
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(file)

