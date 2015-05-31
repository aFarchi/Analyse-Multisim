#____________________
# readDefaultFiles.py
#____________________

from ..path.modulePath import ModulePath

#__________________________________________________

def readLines(fileName):
    try:
        f = open(fileName, 'r')
        l = f.readlines()
        f.close()
        return l
    except:
        print('Could not read file : '+fileName)
        return []

#__________________________________________________

def readDefaultPythonLauncher():
    mp = ModulePath()
    return readLines(mp.defaultPythonLauncher)

#__________________________________________________

def readDefaultBashLauncher():
    mp = ModulePath()
    return readLines(mp.defaultBashLauncher)

#__________________________________________________

def readDefaultNodesFile():
    mp = ModulePath()
    return readLines(mp.defaultNodesFile)

#__________________________________________________
