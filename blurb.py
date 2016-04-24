import os
import subprocess
import time

date = time.strftime("%A") + " " + time.strftime('%B') + " " + time.strftime('%d') +", " + time.strftime('%Y') + " "+ time.strftime('%I') + ":" + time.strftime('%M') + ' ' + time.strftime('%p')
text = None


if text is None:
    text = input("Blurb:")


length = len(text)

while length > 140:
    text = input("Blurb too long("+str(length)+" chars):")
    length = len(text)

command = 't update "'+ text +'"'
status, output = subprocess.getstatusoutput(command)

with open("_data/blurbs.yml") as f:
    contents = f.readlines()
contents.insert(0,"- date: "+ str(date) + "\n  text: " +str(text)+"\n")
f = open("_data/blurbs.yml", "w")
contents = "".join(contents)
f.write(contents)
f.close()
