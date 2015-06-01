#__________________
# writeLaunchers.py
#__________________

from ..sys.run           import makeExe
from readDefaultFiles    import readDefaultPythonLauncher
from readDefaultFiles    import readDefaultBashLauncher
from readDefaultFiles    import readDefaultNodesFile
from write               import writeLinesFillingWithArgs

#__________________________________________________

def writeDefaultPythonLauncher(fileName, args, makeExecutable=True, printIO=False):
    writeLinesFillingWithArgs(readDefaultPythonLauncher(), fileName, args)
    if makeExecutable:
        makeExe(fileName, printIO)

#__________________________________________________

def writeDefaultBashLauncher(fileName, args, makeExecutable=True, printIO=False):
    writeLinesFillingWithArgs(readDefaultBashLauncher(), fileName, args)
    if makeExecutable:
        makeExe(fileName, printIO)

#__________________________________________________
    
def writeDefaultNodesFile(fileName):
    writeLinesFillingWithArgs(readDefaultNodesFile(), fileName, {})

#__________________________________________________
