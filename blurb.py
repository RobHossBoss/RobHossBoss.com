import subprocess
import time

date = time.strftime("%A") + " " + time.strftime('%B') + " " + time.strftime('%d') +", " + time.strftime('%Y') + " "+ time.strftime('%I') + ":" + time.strftime('%M') + ' ' + time.strftime('%p') 
text = raw_input("Blurb:")


with open("_data/blurbs.yml") as f:
    contents = f.readlines()
print contents
contents.insert(0,"- date: "+ str(date) + "\n  text: " +str(text)+"\n")
f = open("_data/blurbs.yml", "w")
contents = "".join(contents)
f.write(contents)
f.close()
