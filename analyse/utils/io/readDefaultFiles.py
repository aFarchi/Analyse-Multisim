#____________________
# readDefaultFiles.py
#____________________

from ..path.modulePath import ModulePath
from read              import readLinesNoFilter

#__________________________________________________

def readDefaultPythonLauncher():
    mp = ModulePath()
    return readLinesNoFilter(mp.defaultPythonLauncher)

#__________________________________________________

def readDefaultBashLauncher():
    mp = ModulePath()
    return readLinesNoFilter(mp.defaultBashLauncher)

#__________________________________________________

def readDefaultNodesFile():
    mp = ModulePath()
    return readLinesNoFilter(mp.defaultNodesFile)

#__________________________________________________

def readDefaultConfigOT2D():
    mp = ModulePath()
    return readLinesNoFilter(mp.defaultConfigOT2D)

#__________________________________________________

def readDefaultConfigPlotOT2D():
    mp = ModulePath()
    return readLinesNoFilter(mp.defaultConfigPlotOT2D)

#__________________________________________________

def readDefaultConfigOTGS():
    mp = ModulePath()
    return readLinesNoFilter(mp.defaultConfigOT1D)

#__________________________________________________

def readDefaultConfigPlotOTGS():
    mp = ModulePath()
    return readLinesNoFilter(mp.defaultConfigPlotOT1D)

#__________________________________________________

