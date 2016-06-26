import os
from PIL import Image

def go():
    countWords()
    resizeImages()
    thumbnail()
    usedImages = getUsedImages()
    removeUsedImages(usedImages)


def countWords():
    path= os.path.abspath(".")+"/_posts"

    for post in os.listdir(path):
        if os.path.isfile(os.path.join(path,post)):
            with open(os.path.join(path,post)) as f:
                contents = f.readlines()
            print contents
            wordCount = 0
            if not contents[4].startswith("time:"):
                for line in contents:
                    wordCount += line.count(' ')
                contents.insert(4, "time: " + str(wordCount / 200) + "\n")
            f = open(os.path.join(path,post), "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()

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
            if width>height:
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
            if width>height:
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


def insertAttribute(attr, line):
    path= os.path.abspath(".")+"/_posts"

    for post in os.listdir(path):
        if os.path.isfile(os.path.join(path,post)):
            with open(os.path.join(path,post)) as f:
                contents = f.readlines()
            contents.insert(line, attr+"\n")
            f = open(os.path.join(path,post), "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()

#insertAttribute('description:', 8)
go()
