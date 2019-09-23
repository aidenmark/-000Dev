# Aeriel Denmark
# Jonny Dailey
# #000Dev
# Tues 9/17/2019

import os
import datetime
import os.path
import shutil

path = os.path.expanduser("~/Desktop")
os.chdir(path)

w = "Wakanda Forever/"

currentDT = datetime.datetime.now().strftime("%m/%d/%Y - %H:%M")

if os.path.exists(w):
    print "It exists"
    os.chdir(w)
    print cwd
    f = open("index.html", "w+")
    f.write(currentDT)
    f.close()
else:
    print "It does not exist."
    print ""
    os.mkdir(w)
    os.chdir(w)
    print "Directory Created."
    f = open("index.html", "w+")
    f.write(currentDT)
    f.close()
