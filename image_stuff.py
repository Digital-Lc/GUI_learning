from __future__ import print_function

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

running = True
while running:
    imagepath = input("What is the name of the image file? ")
    try:
        im = Image.open(imagepath)
    except IOError:
        print("Cannot read file")

    value = float(input("I can adjust contrast, give me a value from 0 to 1"))
    im = ImageEnhance.Contrast(im).enhance(float(value))
    im.save("enhanced.jpg")
    running = False
