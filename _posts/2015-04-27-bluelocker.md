---
layout: page
title:  "Introducing BluLocker"
date:   2015-04-27 13:34:17 -0500
time: 3
categories: Project
image: blulocker-bg
permalink: blulocker
description: BluLocker is a bluetooth proximity locking utility for Windows. Built in Python and availible on Github.
---
The story behind BluLocker began a few months ago when I left my dorm room full of "friends" to run to the cafe and grab a delicious wrap before we began our planned movie night. I slipped on my shoes grabbed my keys, college ID, and phone and stepped out of the room leaving my computer unlocked. Upon my return, my friends are trying to keep it together as I wake my computer to start the movie and find that my desktop wallpaper has been replaced with an admittedly glorious picture of a shirtless Nicholas Cage sprawled, sensually on the moon's surface. They also posted unmentionable Nick Cage photos and quotes on my Facebook profile.

While this was a harmless prank, I began to realize the importance of computer security and began to make a habit of locking my computer when leaving. I wanted to automate this process. I began looking for a Bluetooth pairing program that would lock/unlock when a paired Bluetooth device went out and came into range. I found [BTProximity](http://www.daveamenta.com/btproximity/), an application that accomplished this exactly. But after days of practicing my Google skills, I could not find a working download and eventually came to the conclusion that the program was discontinued. Upon further research, I found [BtProx](http://btprox.sourceforge.net/). I was able to download it but for the life of me, I could not get it to work. I found other similar programs but they had huge license fees. I also found [Gatekeeper](http://www.gkchain.com/) but it only works with a proprietary Bluetooth key chain accessory. I decided that there was a need for such a program as I couldn't find anything similar. I was also enrolled in a software design course and deemed that I could create a program that did this using Python.

### BluLocker Pitch Video

<iframe src="https://www.youtube.com/embed/V4DPvGBrVc8" allowfullscreen="" width="100%" frameborder="0" height="400px"></iframe>

I also had a final project due for this course in about a month and pitched my idea to the professors to see if it qualified as a final project. They approved it but cautioned that I may be getting into something bigger than I could handle. My professors were half-right. Initially, I wanted to unlock the computer when the phone or Bluetooth device came back into range. Also, I wanted to run the program from the system tray. Unlocking the PC required knowledge way to far above my understanding to achieve and running the program in the background is not a native feature of Tkinter, the GUI (Graphical User Interface) back-end I used to program my utility which I named BluLocker. I also came across an issue with Bluetooth pairing. I couldn't figure out how to truly pair to a device using PyBluez, the Python module that I downloaded to handle the Bluetooth side of the program. Instead, for my working model, I simply kept scanning for local devices and when the selected device was not in the list of discoverable devices, the computer locked. That's it.

![BluLocker GUI](/img/post/blulocker1.jpg)

It's a very crude first prototype but it was all that I could complete in the month of time I had to work on it and enough to turn in and hopefully receive a good mark on it. I certainly will continue to work on BluLocker and release it open source and free. I think this is a great project for a beginning programmer to work on as it combines a GUI with networking and windows OS understanding. I wish to accomplish my original intentions and make BluLocker the ultimate security tool. At least for locking your computer and protecting from unsuspecting "Cages".
coming years until they are nearly as ubiquitous as smartphones.
