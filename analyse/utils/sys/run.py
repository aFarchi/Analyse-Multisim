#_______
# run.py
#_______

import os
import sys

#__________________________________________________

def runCommand(command, printIO):
    status = os.system(command)
    if printIO:
        print(command)
    if status != 0:
        print('Could not run command :'+command)
        sys.exit(status)

#__________________________________________________

def makeExe(fileName, printIO=False):
    runCommand('chmod +x '+fileName, printIO)

#__________________________________________________
