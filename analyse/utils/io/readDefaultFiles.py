#____________________
# readDefaultFiles.py
#____________________

from ..path.absolutePath import *

#__________________________________________________

def readLines(fileName, 'r'):
    try:
        f = open(fileName)
        l = f.readlines()
        f.close()
        return l
    except:
        print('Could not read file : '+fileName)
        return []

#__________________________________________________

def readDefaultPythonLauncher():
    return readLines(defaultPythonLauncher())

#__________________________________________________

def readDefaultBashLauncher():
    return readLines(defaultBashLauncher())

#__________________________________________________

def readDefaultNodesFile():
    return readLines(defaultNodesFile())

#__________________________________________________
