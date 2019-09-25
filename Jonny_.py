# Aeriel Denmark
# Jonny Dailey
# #000Dev
# Tues 9/17/2019

import os
import datetime
import os.path
import shutil

# 'shutil' helps to automate copying files and directories; saves the steps of opening, reading,
# writing and closing files when there is no actual processing

path = os.path.expanduser("~/Desktop")
os.chdir(path)

w = "Wakanda Forever/"

currentDT = datetime.datetime.now().strftime("%m/%d/%Y - %H:%M")

template = """
<!DOCTYPE html>
<head>
</head>
<body>
</body>
</html>
"""

if os.path.exists(w):
    print("It exists")
    os.chdir(w) #change user's directory to wanted directory
    print(cwd) #necessary for trobleshooting purposes
    f = open("index.html", "w+")
    f.write(currentDT)
    f.write(template) #why doesn't this work ???!!!
    f.close()
else:
    print("It does not exist.")
    print("")
    os.mkdir(w) #make the directory on the user's desktop
    os.chdir(w) #change directory to newly created directory on user's desktop
    print("Directory Created.") #necessary checkpoint in troubleshooting process
    f = open("index.html", "w+")
    f.write(currentDT)
    f.write(template) #why doesn't this work ???!!!
    f.close()
