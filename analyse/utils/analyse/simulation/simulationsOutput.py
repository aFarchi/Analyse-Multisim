#_____________________
# simulationsOutput.py
#_____________________

from ...path.modulePath             import ModulePath
from ..io.readLists                 import readFileProcesses
from ..io.readLists                 import readFileMinValues
from ..io.readLists                 import readFileLevels
from ..io.readLists                 import readFileLabels
from ..fields.defineFields          import defineFields
from ..timeSelection.defaultTSelect import makeSelectXtimesNt
from simulationsConfiguration       import SimulationsConfiguration
#__________________________________________________

def buildSimulationsOutput(config):
    try:
        funTSelect = makeSelectXtimesNt(config.xTSelect)
    except:
        funTSelect = None

    return SimulationsOutput(config.outputDir,
                             config.sessionName,
                             config.workName,
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
        self.fileLabels    = self.outputDir + self.sessionName + 'list_labels.dat'

        #_________________________

        self.workingDir    = self.outputDir + self.sessionName + self.workName
        self.statDir       = self.workingDir + 'statistics/'
        self.scalingDir    = self.workingDir + 'scaling/'
        self.launcherDir   = self.workingDir + 'launchers/'
        self.figDir        = self.workingDir + 'figures/'

        #_________________________

        self.simConfig     = SimulationsConfiguration(self.configDir)
        self.procList      = readFileProcesses(self.fileProcesses)
        self.minValues     = readFileMinValues(self.fileMinValues)
        self.levels        = readFileLevels(self.fileLevels)
        self.labelList     = readFileLabels(self.fileLabels)
        self.funTSelect    = funTSelect

        self.fieldList     = defineFields(self)

        #_________________________

        self.launcherPreprocessRawDataDir    = self.launcherDir + 'preprocess/preprocessRawData/'
        self.pythonLauncherPreprocessRawData = self.launcherPreprocessRawDataDir + 'preprocessRawData.py'
        self.bashLauncherPreprocessRawData   = self.launcherPreprocessRawDataDir + 'preprocessRawData.sh'
        self.fileProcessesPreprocessRawData  = self.launcherPreprocessRawDataDir + 'processesPreprocessRawData.dat'
        self.configFilePreprocessRawData     = self.launcherPreprocessRawDataDir + 'preprocessRawData.cfg'
        self.fileLogPreprocessRawData        = self.launcherPreprocessRawDataDir + 'logPreprocessRawData'
        self.fileNodesPreprocessRawData      = self.launcherPreprocessRawDataDir + 'nodesPreprocessRawData.dat'


        #_________________________

        self.launcherPlotSimulationDir    = self.launcherDir + 'plotting/simulation/'
        self.pythonLauncherPlotSimulation = self.launcherPlotSimulationDir + 'plotSimulation.py'
        self.bashLauncherPlotSimulation   = self.launcherPlotSimulationDir + 'plotSimulation.sh'
        self.fileProcessesPlotSimulation  = self.launcherPlotSimulationDir + 'processesPlotSimulation.dat'
        self.configFilePlotSimulation     = self.launcherPlotSimulationDir + 'plotSimulation.cfg'
        self.fileLogPlotSimulation        = self.launcherPlotSimulationDir + 'logPlotSimulation'
        self.fileNodesPlotSimulation      = self.launcherPlotSimulationDir + 'nodesPlotSimulation.dat'

        #_________________________

        self.simulationfigDir = self.figDir + 'simulation/'

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

    #_________________________

    def simOutputFieldFigDir(self, AOG, field, lol, species):
        return ( self.simulationfigDir + AOG + field.name + '/' + lol + '/' + species + '/' )

#__________________________________________________
'''

def figDir(outputDir, sessionName, workSession):
    return workingDir(outputDir, sessionName, workSession) + 'figures/'

def figSimulationOutputDir(outputDir, sessionName, workSession, AOG, fieldName, lol, species):
    return figDir(outputDir, sessionName, workSession) + 'simulationOutput/' + AOG + fieldName + '/' + lol + '/' + species + '/'

def figNameSimulationOutputAllSim(outputDir, sessionName, workSession, AOG, fieldName, lol, species):
    return figSimulationOutputDir(outputDir, sessionName, workSession, AOG, fieldName, lol, species) + 'allSim'
'''
