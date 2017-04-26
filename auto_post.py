'''
---
layout: page
title:  "Ultimate Tech Backpack"
date:   2015-04-08 13:34:17 -0500
time:
categories:
image:
permalink:
description: How I made a backpack tech hub. Rechargeable battery bank and solar power charging. Made from an ordinary backpack with parts from Amazon.
---
'''
import sys
import datetime
import yaml
import io
import os
from PIL import Image

def main():
  new_post()
  cleanUp()

def cleanUp():
    resizeImages()
    thumbnail()
    usedImages = getUsedImages()
    removeUsedImages(usedImages)

def thumbnail():
    resize_method = Image.BILINEAR
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter


    max_height= 1000
    max_width= 400
    extensions= ['JPG']

    path= os.path.abspath(".")+"/img/unused"

    def adjusted_size(width,height):
        if width>max_width or height>max_height:
            if width>=height:
                return max_width, int (max_width * height/ width)
            else:
                return int (max_height*width/height), max_height
        else:
            return width,height

    if __name__ == "__main__":
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path,f)):
                f_text, f_ext= os.path.splitext(f)
                f_ext= f_ext[1:].upper()
                if f_ext in extensions:
                    print f
                    image = Image.open(os.path.join(path,f))
                    width, height= image.size
                    image = image.resize(adjusted_size(width, height))
                    image.save(os.path.join(os.path.abspath(".")+"/img/thumbnail",f))

def resizeImages():
    resize_method = Image.ANTIALIAS
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter


    max_height= 99999999
    max_width= 1200
    extensions= ['JPG', 'JPEG', 'PNG']

    path= os.path.abspath(".")+"/img/unused"

    def adjusted_size(width,height):
        if width>max_width or height>max_height:
            if width>=height:
                return max_width, int (max_width * height/ width)
            else:
                return int (max_height*width/height), max_height
        else:
            return width,height

    if __name__ == "__main__":
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path,f)):
                f_text, f_ext= os.path.splitext(f)
                f_ext= f_ext[1:].upper()
                if f_ext in extensions:
                    print f
                    image = Image.open(os.path.join(path,f))
                    width, height= image.size
                    image = image.resize(adjusted_size(width, height) )
                    image.save(os.path.join(os.path.abspath(".")+"/img/cover",f))



def getUsedImages():
    path= os.path.abspath(".")+"/_posts"    
    usedImages = []
    for post in os.listdir(path):
        if os.path.isfile(os.path.join(path,post)):
            with open(os.path.join(path,post)) as f:
                contents = f.readlines()
                usedImages.append(contents[6][6:].strip().replace('"', ''))
    return usedImages

def removeUsedImages(usedImages):
    for image in usedImages:
        path = os.path.join(os.path.abspath(".")+"/img/unused",image+".jpg")
        if os.path.isfile(path):
            os.remove(path)

def new_post():
    date = datetime.datetime.now()
    date = str(date.year) + "-" + str(date.month).zfill(2) + "-" + str(date.day).zfill(2)
    title = raw_input("Title: ")
    c=0
    for i in get_cats():
        print "["+str(c)+"] "+i 
        c+=1  
    category = raw_input("\nCategory: ")
    category = get_cats()[int(category)]
    image = raw_input("Image: ")
    permalink = raw_input("Permalink: ")
    description = raw_input("Description: ")
    file_name = raw_input("Content File Path: ")
    with open(file_name, 'r') as content_file:
        content = content_file.read()
    time = time_count(content)
    post_contents = "---\nlayout: page\ntitle: '"+title+"'\ndate:"+date+" 13:34:17 -0500\ntime:"+str(time)+"\ncategories: "+category+"\nimage:"+image+"\npermalink: "+permalink+"\ndescription:"+description+"\n---\n"+content
    out_file = "_posts/"+date+"-"+title.replace(" ","_")+".md"
    with open(out_file, 'a') as the_file:
        the_file.write(post_contents)

def time_count(contents):
    words = contents.count(" ")
    return int(round(words/250))

def get_cats():
    with open("_data/portfolio.yml", 'r') as stream:
        data_loaded = yaml.load(stream)
    cats = []
    for i in data_loaded['Categories']:
        cats.append(i['name'])
    return cats

def create_cat(cat):
    # Read YAML file
    with open("_data/portfolio.yml", 'r') as stream:
        data_loaded = yaml.load(stream)
        data_loaded['Categories'].append({'name':cat})
    # Write YAML file
    with io.open('_data/portfolio.yml', 'w', encoding='utf8') as outfile:
        yaml.dump(data_loaded, outfile, default_flow_style=False, allow_unicode=True)


main()