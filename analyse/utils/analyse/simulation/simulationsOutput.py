#_____________________
# simulationsOutput.py
#_____________________


from ...path.modulePath       import ModulePath
from ..io.readLists           import readFileProcesses
from ..io.readLists           import readFileMinValues
from ..io.readLists           import readFileLevels
from ..fields.defineFields    import defineFields
from simulationsConfiguration import SimulationsConfiguration
#__________________________________________________

class SimulationsOutput:

    def __init__(self, outputDir, sessionName, workName, funTSelect=None):

        self.modulePath  = ModulePath()
        self.outputDir   = outputDir
        self.sessionName = sessionName
        self.workName    = workName

        #_________________________

        self.configDir     = self.outputDir + self.sessionName + 'config/'
        self.fileMinValues = self.configDir + 'min_values.dat'
        self.fileProcesses = self.outputDir + self.sessionName + 'list_processes.dat'
        self.fileLevels    = self.configDir + 'levels.dat'

        #_________________________

        self.workingDir    = self.outputDir + self.sessionName + self.workName

        self.statDir       = self.workingDir + 'statistics/'
        self.scalingDir    = self.workingDir + 'scaling/'

        #_________________________

        self.simConfig     = SimulationsConfiguration(self.configDir)
        self.procList      = readFileProcesses(self.fileProcesses, prefix, suffix)
        self.minValues     = readFileMinValues(self.fileMinValues)
        self.levels        = readFileLevels(self.fileLevels)
        
        self.fieldList     = defineFields(self)

    #_________________________

    def procOutputDir(self, proc):
        return ( self.outputDir + self.sessionName + proc + '/' )

    def fileSpeciesBin(self, proc, DOW, IOB, speciesBin):
        return ( self.procOutputDir(proc) + DOW + IOB + speciesBin + '.bin' )

    #_________________________

    def scalingFieldDir(self, AOG, field, lol):
        return self.scalingDir + AOG + field.name + '/' + lol + '/'

    def fileScalingFieldSpecies(self, AOG, field, lol, species):
        return self.scalingFieldDir(AOG, field, lol) + species + '.npy'

    def fileFMScalingFieldSpecies(self, AOG, field, lol, species):
        return self.scalingFieldDir(AOG, field,lol) + species + '_FM.npy'


'''
def preprocessedDataProcDir(outputDir, sessionName, workSession, proc):
    return workingDir(outputDir, sessionName, workSession) + proc '/'

def preprocessedDataFieldDir(outputDir, sessionName, workSession, proc, AOG, fieldName, lol):
    return preprocessedDataProcDir(outputDir, sessionName, workSession, proc) + AOG + fieldName + '/' + lol + '/'


#def fileToAnalyse(proc, AOG, fieldName, lol, species):
#    return toAnalyseDir(proc, AOG, fieldName, lol) + species + '.npy'

#def fileGSToAnalyse(proc, AOG, fieldName, lol, species, TS):
#    return toAnalyseDir(proc, AOG, fieldName, lol) + species + '_greyScale' + TS + '.npy'


    

def launcherDir(outputDir, sessionName, workSession):
    return workingDir(outputDir, sessionName, workSession) + 'launchers/'

def launcherPreprocessRDDir(outputDir, sessionName, workSession):
    return launcherDir(outputDir, sessionName, workSession) + 'preprocessRawData/'

def pythonLauncherPreprocessRD(outputDir, sessionName, workSession):
    return launcherPreprocessRDDir(outputDir, sessionName, workSession) + 'preprocessRawData.py'

def bashLauncherPreprocessRD(outputDir, sessionName, workSession):
    return launcherPreprocessRDDir(outputDir, sessionName, workSession) + 'preprocessRawData.sh'

def fileProcessesPreprocessRD(outputDir, sessionName, workSession):
    return launcherPreprocessRDDir(outputDir, sessionName, workSession) + 'processesPreprocessRawData.sh'

def configFilePreprocessRD(outputDir, sessionName, workSession):
    return launcherPreprocessRDDir(outputDir, sessionName, workSession) + 'preprocessRawData.cfg'

def fileLogPreprocessRD(outputDir, sessionName, workSession):
    return launcherPreprocessRDDir(outputDir, sessionName) + 'logPreprocessRawData'

def fileNodesPreprocessRD(outputDir, sessionName, workSession):
    return launcherPreprocessRDDir(outputDir, sessionName, workSession) + 'nodesPreprocessRawData.dat'

def figDir(outputDir, sessionName, workSession):
    return workingDir(outputDir, sessionName, workSession) + 'figures/'

def figSimulationOutputDir(outputDir, sessionName, workSession, AOG, fieldName, lol, species):
    return figDir(outputDir, sessionName, workSession) + 'simulationOutput/' + AOG + fieldName + '/' + lol + '/' + species + '/'

def figNameSimulationOutputAllSim(outputDir, sessionName, workSession, AOG, fieldName, lol, species):
    return figSimulationOutputDir(outputDir, sessionName, workSession, AOG, fieldName, lol, species) + 'allSim'
'''
