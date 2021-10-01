#!/usr/bin/python

import sys
import os
import random
from flask import Flask, render_template
from image_slicer import slice, join, Image
import shuffle

app = Flask(__name__)


#get stock price
stockprice = 50

#import all images
all_image_pool = [ ]
#images already used
image_pool_used = [ ] #keep a DB of the images already used
 
#remove images already used from image_pool
image_pool = [ ] #remove image_pool_used from image_pool

#image_profit = random.choice(image_pool)
image_pool = [ ] #remove image_profit from image_pool

#image_loss = random.choice(image_pool)
image_pool = [ ] #remove image_loss from image_pool


#scramble image into 16 tiles (4x4)
# tiles = slice('test.JPG',16)
# image = join(tiles)
# image.save('join.png')

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

    im2.save("profit_shuf" + origname)
    
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

    im2.save("loss_shuf" + origname)


profit_image = shuffle.shuffle_pic_profit('test.jpg')
loss_image = shuffle.shuffle_pic_loss('test2.jpg')



### WEB ROUTES ###

# /
@app.route('/')
@app.route('/index')
def show_index():
    return render_template("index.html")#, profit_image = 'profit_image.jpg', loss_image = 'loss_image.jpg')