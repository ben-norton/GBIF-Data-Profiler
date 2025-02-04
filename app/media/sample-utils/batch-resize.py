from PIL import Image
import os, sys

# Batch Resize with Maintain Ratio
# Source: https://gist.github.com/makomweb/88c9cc398159390e8a2fa1beda5dcfed

path = "c:\\Workspace\Images"
dirs = os.listdir( path )
mywidth = 640

def resize_keep_aspect_ration():
    for item in dirs:
        img_path = path + "\\" + item
        if os.path.isfile(img_path):
            im = Image.open(img_path)
            f, e = os.path.splitext(img_path)
            wpercent = (mywidth / float(im.size[0]))
            hsize = int((float(im.size[1]) * float(wpercent)))

            im = im.resize((mywidth, hsize), Image.ANTIALIAS)
            im.save(f + '.png', 'PNG')

resize_keep_aspect_ration()