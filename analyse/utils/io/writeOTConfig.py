#__________________
# writeLaunchers.py
#__________________

from readDefaultFiles    import readDefaultConfigOT2D
from write               import writeLinesFillingWithArgs

#__________________________________________________

def writeDefaultConfigOT2D(fileName, args):
    writeLinesFillingWithArgs(readDefaultConfigOT2D(), fileName, args)

#__________________________________________________
