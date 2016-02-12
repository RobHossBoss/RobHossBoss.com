import os

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
