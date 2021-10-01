#!/usr/bin/python

import sys
import random
from image_slicer import Image

def shuffle_pic_profit(image):
    origname = image#sys.argv[1]

    im = Image.open(origname)
    width, height = im.size
    width = (int(width + 99) / 100) * 100
    height = (int(height + 99) / 100) * 100
    widthint = int(width)
    heightint = int(height)
    im = im.crop((0, 0, width, height))

    im2 = Image.new("RGB", (widthint, heightint), "black")

    blocks = []
    for x in range(widthint // 100):
        for y in range(heightint // 100):
            blocks.append(im.crop((x * 100, y * 100, (x + 1) * 100, (y + 1) * 100)))

    random.shuffle(blocks)

    for x in range(widthint // 100):
        for y in range(heightint // 100):
            im2.paste(blocks.pop().rotate(90 * random.randint(0,3)), (x * 100, y * 100))

    im2.save("./static/profit_shuf" + origname)
    
def shuffle_pic_loss(image):
    origname = image#sys.argv[1]

    im = Image.open(origname)
    width, height = im.size
    width = (int(width + 99) / 100) * 100
    height = (int(height + 99) / 100) * 100
    widthint = int(width)
    heightint = int(height)
    im = im.crop((0, 0, width, height))

    im2 = Image.new("RGB", (widthint, heightint), "black")

    blocks = []
    for x in range(widthint // 100):
        for y in range(heightint // 100):
            blocks.append(im.crop((x * 100, y * 100, (x + 1) * 100, (y + 1) * 100)))

    random.shuffle(blocks)

    for x in range(widthint // 100):
        for y in range(heightint // 100):
            im2.paste(blocks.pop().rotate(90 * random.randint(0,3)), (x * 100, y * 100))

    im2.save("./static/loss_shuf" + origname)