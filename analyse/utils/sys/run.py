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
        sys.exit(status)

#__________________________________________________
