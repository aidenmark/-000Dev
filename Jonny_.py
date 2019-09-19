# Aeriel Denmark
# Jonny Dailey
# #000Dev
# Tues 9/17/2019

import os
import datetime

path = os.path.expanduser("~/Desktop")
os.chdir(path)

#Time needs to be converted into a string, research 'strftime' and tell me what it does.
currentDT = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# 'strftime' is a method that basically takes 'datetime' and turn it into a string to make it human readable
# 'strptime' does the opposite

newfolder = os.mkdir("Wakanda Forever")

path = os.path.expanduser("~/Desktop/Wakanda Forever")

os.chdir(path)

f= open("index.html", "w+")

f.write(currentDT)
f.close()
