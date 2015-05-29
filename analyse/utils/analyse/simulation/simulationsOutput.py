#_____________________
# simulationsOutput.py
#_____________________

from ...path.modulePath             import ModulePath
from ..io.readLists                 import readFileProcesses
from ..io.readLists                 import readFileMinValues
from ..io.readLists                 import readFileLevels
from ..fields.defineFields          import defineFields
from simulationsConfiguration       import SimulationsConfiguration
from ..timeSelection.defaultTSelect import makeSelectXtimesNt

#__________________________________________________

def buildSimulationsOutput(preprocessConfig):
    funTSelect = makeSelectXtimesNt(preprocessConfig.xTSelect)
    return SimulationsOutput(preprocessConfig.outputDir,
                             preprocessConfig.sessionName,
                             preprocessConfig.workName,
                             funTSelect)

#__________________________________________________

class SimulationsOutput:

    def __init__(self, outputDir, sessionName, workName, funTSelect=None):

        self.modulePath    = ModulePath()
        self.outputDir     = outputDir
        self.sessionName   = sessionName
        self.workName      = workName

        #_________________________

        self.configDir     = self.outputDir + self.sessionName + 'config/'
        self.fileMinValues = self.configDir + 'min_values.dat'
        self.fileProcesses = self.outputDir + self.sessionName + 'list_processes.dat'
        self.fileLevels    = self.configDir + 'levels.dat'

        #_________________________

        self.workingDir    = self.outputDir + self.sessionName + self.workName
        self.statDir       = self.workingDir + 'statistics/'
        self.scalingDir    = self.workingDir + 'scaling/'
        self.launcherDir   = self.workingDir + 'launchers/'
        #_________________________

        self.simConfig     = SimulationsConfiguration(self.configDir)
        self.procList      = readFileProcesses(self.fileProcesses, prefix, suffix)
        self.minValues     = readFileMinValues(self.fileMinValues)
        self.levels        = readFileLevels(self.fileLevels)
        
        self.fieldList     = defineFields(self)

        #_________________________

        self.launcherPreprocessRawDataDir    = self.launcherDir + 'preprocessRawData/'
        self.pythonLauncherPreprocessRawData = self.launcherPreprocessRawDataDir + 'preprocessRawData.py'
        self.bashLauncherPreprocessRawData   = self.launcherPreprocessRawDataDir + 'preprocessRawData.sh'
        self.fileProcessesPreprocessRawData  = self.launcherPreprocessRawDataDir + 'processesPreprocessRawData.data'
        self.configFilePreprocessRawData     = self.launcherPreprocessRawDataDir + 'preprocessRawData.cfg'
        self.fileLogPreprocessRawData        = self.launcherPreprocessRawDataDir + 'logPreprocessRawData'
        self.fileNodesPreprocessRawData      = self.launcherPreprocessRawDataDir + 'nodesPreprocessRawData.dat'

    #_________________________

    def procOutputDir(self, proc):
        return ( self.outputDir + self.sessionName + proc + '/' )

    def fileSpeciesBinProc(self, proc, DOW, IOB, speciesBin):
        return ( self.procOutputDir(proc) + DOW + IOB + speciesBin + '.bin' )

    #_________________________

    def scalingFieldDir(self, AOG, field, lol):
        return ( self.scalingDir + AOG + field.name + '/' + lol + '/' )

    def fileScalingFieldSpecies(self, AOG, field, lol, species):
        return ( self.scalingFieldDir(AOG, field, lol) + species + '.npy' )

    def fileFMScalingFieldSpecies(self, AOG, field, lol, species):
        return ( self.scalingFieldDir(AOG, field,lol) + species + '_FM.npy' )

    #_________________________

    def procPreprocessedDataDir(self, proc):
        return ( self.workingDir + proc + '/' )

    def procPreprocessedFieldDir(self, proc, AOG, field, lol):
        return ( self.procPreprocessedDataDir(proc) + AOG + field.name + '/' + lol + '/' )

    def fileProcPreprocessedField(self, proc, AOG, field, lol, species):
        return ( self.procPreprocessedFieldDir(proc, AOG, field, lol) + species + '.npy' )

    def fileProcPreprocessedFieldGS(self, proc, AOG, field, lol, species, TS):
        return ( self.procPreprocessedFieldDir(proc, AOG, field, lol) + species + 'grayScale' + TS + '.npy' )

#__________________________________________________
'''

def figDir(outputDir, sessionName, workSession):
    return workingDir(outputDir, sessionName, workSession) + 'figures/'

def figSimulationOutputDir(outputDir, sessionName, workSession, AOG, fieldName, lol, species):
    return figDir(outputDir, sessionName, workSession) + 'simulationOutput/' + AOG + fieldName + '/' + lol + '/' + species + '/'

def figNameSimulationOutputAllSim(outputDir, sessionName, workSession, AOG, fieldName, lol, species):
    return figSimulationOutputDir(outputDir, sessionName, workSession, AOG, fieldName, lol, species) + 'allSim'
'''
