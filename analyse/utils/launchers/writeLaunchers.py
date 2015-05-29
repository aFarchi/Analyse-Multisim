#__________________
# writeLaunchers.py
#__________________

from ..sys.run             import makeExe
from ..path.absolutePath   import *
from ..io.readDefaultFiles import readDefaultPythonLauncher
from ..io.readDefaultFiles import readDefaultBashLauncher
from ..io.readDefaultFiles import readDefaultNodesFile
from ..io.write            import writeLinesFillingWithArgs
#__________________________________________________

def writeDefaultPythonLauncher(fileName, args, makeExe=True, printIO=False):
    writeLinesFillingWithArgs(readDefaultPythonLauncher(), fileName, args)
    if makeExe:
        makeExe(fileName, printIO)

#__________________________________________________

def writeDefaultBashLauncher(fileName, args, makeExe=True, printIO=False):
    writeLinesFillingWithArgs(readDefaultBashLauncher(), fileName, args)
    if makeExe:
        makeExe(fileName, printIO)

#__________________________________________________
    
def writeDefaultNodesFile(fileName):
    writeLinesFillingWithArgs(readDefaultNodesFile(), fileName, {})

#__________________________________________________
