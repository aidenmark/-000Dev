# Aeriel Denmark
# Jonny Dailey
# #000Dev
# Tues 9/17/2019

import os
import datetime
import os.path

path = os.path.expanduser("~/Desktop")
os.chdir(path)

newfolder = os.mkdir("Wakanda Forever")
path = os.path.expanduser("~/Desktop/Wakanda Forever")

os.chdir(path)
os.path.exists(path)

currentDT = datetime.datetime.now().strftime("%m/%d/%Y - %H:%M")

if os.path.exists(path):
    f= open("index.html", "w+")
    f.write(currentDT)
    f.close()

else:
    os.chdir(path)
    f= open("index.html", "w+")
    f.write(currentDT)
    f.close()
