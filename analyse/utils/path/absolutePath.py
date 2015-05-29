#________________
# absolutePath.py
#________________

def moduleUpperPath():
    return '/cerea_raid/users/farchia/Analyse-Multisim/'

def modulePath():
    return moduleUpperPath() + 'analyse/'

def moduleLauncher():
    return moduleUpperPath() + 'launcher.py'

def moduleLauncherPlotting():
    return moduleUpperPath() + 'launcherPlotting.py'

def OTmodulePath():
    return '/profils_cerea/farchia/OT/Optimal-Transport/'

#________________

def submoduleLauncherPath():
    return modulePath() + 'utils/launchers/'

def defaultFilesPath():
    return submoduleLauncherPath() + 'defaultFiles/'

def defaultPythonLauncher():
    return defaultFilesPath() + 'defaultLauncher.py'

def defaultBashLauncher():
    return defaultFilesPath() + 'defaultLauncher.sh'

def defaultNodesFile():
    return defaultFilesPath() + 'defaultNodes.dat'
    
#________________

def configDir(outputDir, sessionName):
    return outputDir + sessionName + 'config/'

def fileMinValues(outputDir, sessionName):
    return configDir(outputDir, sessionName) + 'min_values.dat'

def fileProcesses(outputDir, sessionName):
    return outputDir + sessionName + 'list_processes.dat'

def fileLevels(outputDir, sessionName):
    return configDir(outputDir, sessionName) + 'levels.dat'

def toAnalyseDir(proc, AOG, fieldName, lol):
    return proc + 'toAnalyse/' + AOG + fieldName + '/' + lol + '/'

def fileToAnalyse(proc, AOG, fieldName, lol, species):
    return toAnalyseDir(proc, AOG, fieldName, lol) + species + '.npy'

def fileGSToAnalyse(proc, AOG, fieldName, lol, species, TS):
    return toAnalyseDir(proc, AOG, fieldName, lol) + species + '_greyScale' + TS + '.npy'

def statDir(outputDir, sessionName):
    return outputDir + sessionName + 'statistics/'

def scalingDir(outputDir, sessionName, AOG, fieldName, lol):
    return statDir(outputDir, sessionName) + 'scaling/' + AOG + fieldName + '/' + lol + '/'

def fileScaling(outputDir, sessionName, AOG, fieldName, lol, species):
    return scalingDir(outputDir, sessionName, AOG, fieldName, lol) + species + '.npy'

def fileFMScaling(outputDir, sessionName, AOG, fieldName, lol, species):
    return scalingDir(outputDir, sessionName, AOG, fieldName, lol) + species + '_FM.npy'
    
def launcherDir(outputDir, sessionName):
    return outputDir + sessionName + 'launchers/'

def launcherPreprocessRDDir(outputDir, sessionName):
    return launcherDir(outputDir, sessionName) + 'preprocessRawData/'

def pythonLauncherPreprocessRD(outputDir, sessionName):
    return launcherPreprocessRDDir(outputDir, sessionName) + 'preprocessRawData.py'

def bashLauncherPreprocessRD(outputDir, sessionName):
    return launcherPreprocessRDDir(outputDir, sessionName) + 'preprocessRawData.sh'

def fileProcessesPreprocessRD(outputDir, sessionName):
    return launcherPreprocessRDDir(outputDir, sessionName) + 'processesPreprocessRawData.sh'

def configFilePreprocessRD(outputDir, sessionName):
    return launcherPreprocessRDDir(outputDir, sessionName) + 'preprocessRawData.cfg'

def fileLogPreprocessRD(outputDir, sessionName):
    return launcherPreprocessRDDir(outputDir, sessionName) + 'logPreprocessRawData'

def fileNodesPreprocessRD(outputDir, sessionName):
    return launcherPreprocessRDDir(outputDir, sessionName) + 'nodesPreprocessRawData.dat'

def figDir(outputDir, sessionName):
    return outputDir + sessionName + 'figures/'

def figSimulationOutputDir(outputDir, sessionName, AOG, fieldName, lol, species):
    return figDir(outputDir, sessionName) + 'simulationOutput/' + AOG + fieldName + '/' + lol + '/' + species + '/'

def figNameSimulationOutputAllSim(outputDir, sessionName, AOG, fieldName, lol, species):
    return figSimulationOutputDir(outputDir, sessionName, AOG, fieldName, lol, species) + 'allSim'
