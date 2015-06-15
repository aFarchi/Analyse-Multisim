#_____________________
# simulationsOutput.py
#_____________________

from ...path.modulePath             import ModulePath
from ..io.readLists                 import readFileProcesses
from ..io.readLists                 import readFileMinValues
from ..io.readLists                 import readFileLevels
from ..io.readLists                 import readFileLabels
from ..io.navigate                  import *
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
        self.OTDir         = self.workingDir + 'optimalTransport/'
        self.OT2DDir       = self.OTDir + 'OT2D/'
        self.OTGSDir       = self.OTDir + 'OTGS/'
        self.applyOTGSDir  = self.OTDir + 'applyOTGS/'

        #_________________________

        self.simConfig     = SimulationsConfiguration(self.configDir)
        self.procList      = readFileProcesses(self.fileProcesses)
        self.minValues     = readFileMinValues(self.fileMinValues)
        self.levels        = readFileLevels(self.fileLevels)
        self.labelList     = readFileLabels(self.fileLabels)
        self.funTSelect    = funTSelect

        self.fieldList     = defineFields(self)

        #_________________________

        self.launcherPreprocessRawDataFiles               = {}
        self.launcherPreprocessRawDataFiles['directory']  = self.launcherDir + 'preprocessRawData/' 
        self.launcherPreprocessRawDataFiles['pyLauncher'] = self.launcherPreprocessRawDataFiles['directory'] + 'preprocessRawData.py'
        self.launcherPreprocessRawDataFiles['shLauncher'] = self.launcherPreprocessRawDataFiles['directory'] + 'preprocessRawData.sh'
        self.launcherPreprocessRawDataFiles['processes']  = self.launcherPreprocessRawDataFiles['directory'] + 'processesPreprocessRawData.dat'
        self.launcherPreprocessRawDataFiles['config']     = self.launcherPreprocessRawDataFiles['directory'] + 'preprocessRawData.cfg'
        self.launcherPreprocessRawDataFiles['nodes']      = self.launcherPreprocessRawDataFiles['directory'] + 'nodesPreprocessRawData.dat'
        self.launcherPreprocessRawDataFiles['log']        = self.launcherPreprocessRawDataFiles['directory'] + 'logPreprocessRawData'

        #_________________________

        self.launcherStatisticalAnalyseFiles               = {}
        self.launcherStatisticalAnalyseFiles['directory']  = self.launcherDir + 'statisticalAnalyse/performStatisticalAnalyse/'
        self.launcherStatisticalAnalyseFiles['pyLauncher'] = self.launcherStatisticalAnalyseFiles['directory'] + 'performStatisticalAnalyse.py'
        self.launcherStatisticalAnalyseFiles['shLauncher'] = self.launcherStatisticalAnalyseFiles['directory'] + 'performStatisticalAnalyse.sh'
        self.launcherStatisticalAnalyseFiles['processes']  = self.launcherStatisticalAnalyseFiles['directory'] + 'processesPerformStatisticalAnalyse.dat'
        self.launcherStatisticalAnalyseFiles['config']     = self.launcherStatisticalAnalyseFiles['directory'] + 'performStatisticalAnalyse.cfg'
        self.launcherStatisticalAnalyseFiles['nodes']      = self.launcherStatisticalAnalyseFiles['directory'] + 'nodesPerformStatisticalAnalyse.dat'
        self.launcherStatisticalAnalyseFiles['log']        = self.launcherStatisticalAnalyseFiles['directory'] + 'logPerformStatisticalAnalyse'

        #_________________________

        self.launcherOTDir   = self.launcherDir + 'optimalTransport/'
        self.launcherOTGSDir = self.launcherOTDir + 'OTGS/'
        
        self.launcherInterpolateIntoOTGSResolutionFiles               = {}
        self.launcherInterpolateIntoOTGSResolutionFiles['directory']  = self.launcherOTGSDir + 'interpolateIntoOTGSResolution/'
        self.launcherInterpolateIntoOTGSResolutionFiles['pyLauncher'] = ( self.launcherInterpolateIntoOTGSResolutionFiles['directory'] +
                                                                          'interpolateIntoOTGSResolution.py' )
        self.launcherInterpolateIntoOTGSResolutionFiles['shLauncher'] = ( self.launcherInterpolateIntoOTGSResolutionFiles['directory'] + 
                                                                          'interpolateIntoOTGSResolution.sh' )
        self.launcherInterpolateIntoOTGSResolutionFiles['processes']  = ( self.launcherInterpolateIntoOTGSResolutionFiles['directory'] + 
                                                                          'processesInterpolateIntoOTGSResolution.dat' )
        self.launcherInterpolateIntoOTGSResolutionFiles['config']     = ( self.launcherInterpolateIntoOTGSResolutionFiles['directory'] + 
                                                                          'interpolateIntoOTGSResolution.cfg' )
        self.launcherInterpolateIntoOTGSResolutionFiles['nodes']      = ( self.launcherInterpolateIntoOTGSResolutionFiles['directory'] + 
                                                                          'nodesInterpolateIntoOTGSResolution.dat' )
        self.launcherInterpolateIntoOTGSResolutionFiles['log']        = ( self.launcherInterpolateIntoOTGSResolutionFiles['directory'] + 
                                                                          'logInterpolateIntoOTGSResolution' )

        self.launcherMergeOTGSResultsFiles               = {}
        self.launcherMergeOTGSResultsFiles['directory']  = self.launcherOTGSDir + 'mergeOTGSResults/' 
        self.launcherMergeOTGSResultsFiles['pyLauncher'] = self.launcherMergeOTGSResultsFiles['directory'] + 'mergeOTGSResults.py'
        self.launcherMergeOTGSResultsFiles['shLauncher'] = self.launcherMergeOTGSResultsFiles['directory'] + 'mergeOTGSResults.sh'
        self.launcherMergeOTGSResultsFiles['processes']  = self.launcherMergeOTGSResultsFiles['directory'] + 'processesMergeOTGSResults.dat'
        self.launcherMergeOTGSResultsFiles['config']     = self.launcherMergeOTGSResultsFiles['directory'] + 'mergeOTGSResults.cfg'
        self.launcherMergeOTGSResultsFiles['nodes']      = self.launcherMergeOTGSResultsFiles['directory'] + 'nodesMergeOTGSResults.dat'
        self.launcherMergeOTGSResultsFiles['log']        = self.launcherMergeOTGSResultsFiles['directory'] + 'logMergeOTGSResults'

        self.launcherApplyGSTransportFiles               = {}
        self.launcherApplyGSTransportFiles['directory']  = self.launcherOTGSDir + 'applyGSTransport/'
        self.launcherApplyGSTransportFiles['pyLauncher'] = self.launcherApplyGSTransportFiles['directory'] + 'applyGSTransport.py'
        self.launcherApplyGSTransportFiles['shLauncher'] = self.launcherApplyGSTransportFiles['directory'] + 'applyGSTransport.sh'
        self.launcherApplyGSTransportFiles['processes']  = self.launcherApplyGSTransportFiles['directory'] + 'processesApplyGSTransport.dat'
        self.launcherApplyGSTransportFiles['config']     = self.launcherApplyGSTransportFiles['directory'] + 'applyGSTransport.cfg'
        self.launcherApplyGSTransportFiles['nodes']      = self.launcherApplyGSTransportFiles['directory'] + 'nodesApplyGSTransport.dat'
        self.launcherApplyGSTransportFiles['log']        = self.launcherApplyGSTransportFiles['directory'] + 'logApplyGSTransport'

        self.launcherOT2DDir = self.launcherOTDir + 'OT2D/'

        self.launcherInterpolateIntoOT2DResolutionFiles               = {}
        self.launcherInterpolateIntoOT2DResolutionFiles['directory']  = self.launcherOT2DDir + 'interpolateIntoOT2DResolution/'
        self.launcherInterpolateIntoOT2DResolutionFiles['pyLauncher'] = ( self.launcherInterpolateIntoOT2DResolutionFiles['directory'] +
                                                                          'interpolateIntoOT2DResolution.py' )
        self.launcherInterpolateIntoOT2DResolutionFiles['shLauncher'] = ( self.launcherInterpolateIntoOT2DResolutionFiles['directory'] +
                                                                          'interpolateIntoOT2DResolution.sh' )
        self.launcherInterpolateIntoOT2DResolutionFiles['processes']  = ( self.launcherInterpolateIntoOT2DResolutionFiles['directory'] +
                                                                          'processesInterpolateIntoOT2DResolution.dat' )
        self.launcherInterpolateIntoOT2DResolutionFiles['config']     = ( self.launcherInterpolateIntoOT2DResolutionFiles['directory'] +
                                                                          'interpolateIntoOT2DResolution.cfg' )
        self.launcherInterpolateIntoOT2DResolutionFiles['nodes']      = ( self.launcherInterpolateIntoOT2DResolutionFiles['directory'] +
                                                                          'nodesInterpolateIntoOT2DResolution.dat' )
        self.launcherInterpolateIntoOT2DResolutionFiles['log']        = ( self.launcherInterpolateIntoOT2DResolutionFiles['directory'] +
                                                                          'logInterpolateIntoOT2DResolution' )

        self.launcherMergeOT2DResultsFiles               = {}
        self.launcherMergeOT2DResultsFiles['directory']  = self.launcherOT2DDir + 'mergeOT2DResults/'
        self.launcherMergeOT2DResultsFiles['pyLauncher'] = self.launcherMergeOT2DResultsFiles['directory'] + 'mergeOT2DResults.py'
        self.launcherMergeOT2DResultsFiles['shLauncher'] = self.launcherMergeOT2DResultsFiles['directory'] + 'mergeOT2DResults.sh'
        self.launcherMergeOT2DResultsFiles['processes']  = self.launcherMergeOT2DResultsFiles['directory'] + 'processesMergeOT2DResults.dat'
        self.launcherMergeOT2DResultsFiles['config']     = self.launcherMergeOT2DResultsFiles['directory'] + 'mergeOT2DResults.cfg'
        self.launcherMergeOT2DResultsFiles['nodes']      = self.launcherMergeOT2DResultsFiles['directory'] + 'nodesMergeOT2DResults.dat'
        self.launcherMergeOT2DResultsFiles['log']        = self.launcherMergeOT2DResultsFiles['directory'] + 'logMergeOT2DResults'

        #_________________________

        self.launcherPlotSimulationFiles               = {}
        self.launcherPlotSimulationFiles['directory']  = self.launcherDir + 'plotting/simulation/' 
        self.launcherPlotSimulationFiles['pyLauncher'] = self.launcherPlotSimulationFiles['directory'] + 'plotSimulation.py' 
        self.launcherPlotSimulationFiles['shLauncher'] = self.launcherPlotSimulationFiles['directory'] + 'plotSimulation.sh'
        self.launcherPlotSimulationFiles['processes']  = self.launcherPlotSimulationFiles['directory'] + 'processesPlotSimulation.dat'
        self.launcherPlotSimulationFiles['config']     = self.launcherPlotSimulationFiles['directory'] + 'plotSimulation.cfg'
        self.launcherPlotSimulationFiles['nodes']      = self.launcherPlotSimulationFiles['directory'] + 'nodesPlotSimulation.dat'
        self.launcherPlotSimulationFiles['log']        = self.launcherPlotSimulationFiles['directory'] + 'logPlotSimulation'

        #_________________________

        self.launcherPlotFieldFiles = {}
        self.launcherPlotFieldFiles['directory']  = self.launcherDir + 'plotting/fields/' 
        self.launcherPlotFieldFiles['pyLauncher'] = self.launcherPlotFieldFiles['directory'] + 'plotFields.py'
        self.launcherPlotFieldFiles['shLauncher'] = self.launcherPlotFieldFiles['directory'] + 'plotFields.sh'
        self.launcherPlotFieldFiles['processes']  = self.launcherPlotFieldFiles['directory'] + 'processesPlotFields.dat'
        self.launcherPlotFieldFiles['config']     = self.launcherPlotFieldFiles['directory'] + 'plotFields.cfg'
        self.launcherPlotFieldFiles['nodes']      = self.launcherPlotFieldFiles['directory'] + 'nodesPlotFields.dat'
        self.launcherPlotFieldFiles['log']        = self.launcherPlotFieldFiles['directory'] + 'logPlotFields'

        #_________________________

        self.launcherPlotApplyGSTransportFiles               = {}
        self.launcherPlotApplyGSTransportFiles['directory']  = self.launcherDir + 'plotting/applyGSTransport/'
        self.launcherPlotApplyGSTransportFiles['pyLauncher'] = self.launcherPlotApplyGSTransportFiles['directory'] + 'plotApplyGSTransport.py'
        self.launcherPlotApplyGSTransportFiles['shLauncher'] = self.launcherPlotApplyGSTransportFiles['directory'] + 'plotApplyGSTransport.sh'
        self.launcherPlotApplyGSTransportFiles['processes']  = self.launcherPlotApplyGSTransportFiles['directory'] + 'processesPlotApplyGSTransport.dat'
        self.launcherPlotApplyGSTransportFiles['config']     = self.launcherPlotApplyGSTransportFiles['directory'] + 'plotApplyGSTransport.cfg'
        self.launcherPlotApplyGSTransportFiles['nodes']      = self.launcherPlotApplyGSTransportFiles['directory'] + 'nodesPlotApplyGSTransport.dat'
        self.launcherPlotApplyGSTransportFiles['log']        = self.launcherPlotApplyGSTransportFiles['directory'] + 'logPlotApplyGSTransport'

        #_________________________

        self.simulationfigDir           = self.figDir + 'simulation/'
        self.fieldfigDir                = self.figDir + 'fields/fields/'
        self.fieldAttachGrayScalefigDir = self.figDir + 'fields/fieldsAttachGrayScale/'
        self.OTfigDir                   = self.figDir + 'optimalTransport/'
        self.OT2DfigDir                 = self.OTfigDir + 'OT2D/'
        self.OTGSfigDir                 = self.OTfigDir + 'OTGS/'
        self.applyGSTransportfigDir     = self.OTfigDir + 'applyGSTransport/'

    #_________________________

    def procOutputDir(self, proc):
        return ( self.outputDir + self.sessionName + proc + '/' )

    def fileSpeciesBinProc(self, proc, DOW, IOB, speciesBin):
        return ( self.procOutputDir(proc) + DOW + IOB + speciesBin + '.bin' )

    #_________________________

    def scalingFieldDir(self, AOG, field, LOL):
        return ( self.scalingDir + AOG + field.name + '/' + LOL + '/' )

    def fileScalingFieldSpecies(self, AOG, field, LOL, species):
        return ( self.scalingFieldDir(AOG, field, LOL) + species + '.npy' )

    def fileFMScalingFieldSpecies(self, AOG, field, LOL, species):
        return ( self.scalingFieldDir(AOG, field,LOL) + species + '_FM.npy' )

    #_________________________

    def analyseFieldSeciesDir(self, AOG, field, LOL, species):
        return ( self.statDir + AOG + field.name + '/' + LOL + '/' )

    #_________________________

    def procPreprocessedDataDir(self, proc):
        return ( self.workingDir + proc + '/' )

    def procPreprocessedFieldDir(self, proc, AOG, field, LOL):
        return ( self.procPreprocessedDataDir(proc) + 'rawResolution/' + AOG + field.name + '/' + LOL + '/' )

    def fileProcPreprocessedField(self, proc, AOG, field, LOL, species, TS):
        return ( self.procPreprocessedFieldDir(proc, AOG, field, LOL) + species + '_' + TS + '.npy' )

    def fileProcPreprocessedFieldGS(self, proc, AOG, field, LOL, species, TS):
        return ( self.procPreprocessedFieldDir(proc, AOG, field, LOL) + species + '_grayScale_' + TS + '.npy' )

    #_________________________

    def procPreprocessedFieldOTResolutionDir(self, proc, AOG, field, LOL):
        return ( self.procPreprocessedDataDir(proc) + 'OTResolution/' + AOG + field.name + '/' + LOL + '/' )

    def fileProcPreprocessedFieldOTResolution(self, proc, AOG, field, LOL, species):
        return ( self.procPreprocessedFieldOTResolutionDir(proc, AOG, field, LOL) + species + '.npy' )

    def fileProcPreprocessedFieldGSOTResolution(self, proc, AOG, field, LOL, species, TS):
        return ( self.procPreprocessedFieldOTResolutionDir(proc, AOG, field, LOL) + species + 'grayScale' + TS + '.npy' )

    #_________________________

    def simOutputFieldFigDir(self, AOG, field, LOL, species):
        return ( self.simulationfigDir + AOG + field.name + '/' + LOL + '/' + species + '/' )

    #_________________________

    def fieldFigDir(self, AOG, field, LOL, species):
        return ( self.fieldfigDir + AOG + field.name + '/' + LOL + '/' + species + '/' )

    #_________________________

    def fieldAttachGrayScaleFigDir(self, AOG, field, LOL, species):
        return ( self.fieldAttachGrayScalefigDir + AOG + field.name + '/' + LOL + '/' + species + '/' )

    #_________________________
    
    def launcherPerformOT2DDir(self, configName):
        return ( self.launcherOT2DDir + configName + '/performOT2D/' )

    def fileProcessesPerformOT2D(self, configName):
        return ( self.launcherPerformOT2DDir(configName) + 'processesPerformOT2D.dat' )

    def fileLogPerformOT2D(self, configName):
        return ( self.launcherPerformOT2DDir(configName) + 'logPerformOT2D' )

    def fileNodesPerformOT2D(self, configName):
        return ( self.launcherPerformOT2DDir(configName) + 'nodesPerformOT2D.dat' )

    def pythonLauncherPerformOT2D(self, configName):
        return ( self.launcherPerformOT2DDir(configName) + 'performOT2D.py' )

    def bashLauncherPerformOT2D(self, configName):
        return ( self.launcherPerformOT2DDir(configName) + 'performOT2D.sh' )

    def performOT2DFieldSpeciesDir(self, AOG, field, LOL, species):
        return ( self.OT2DDir + AOG + field.name + '/' + LOL + '/' + species + '/' ) 

    def performOT2DP0P1FieldSpeciesDir(self, configName, p0, p1, AOG, field, LOL, species):
        return ( self.performOT2DFieldSpeciesDir(AOG, field, LOL, species) + str(p0) + '-' + str(p1) + '/' + configName + '/' )

    def configFilePerformOT2DP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species):
        return ( self.performOT2DP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species) + configName + '.cfg' )

    def resultsFileOT2DP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species):
        return ( self.performOT2DP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species) + 'result.bin' )

    def mergedResultsFileOT2DFieldSpecies(self, configName, AOG, field, LOL, species):
        return ( self.performOT2DFieldSpeciesDir(AOG, field, LOL, species) + 'results_'+configName )

    #_________________________
    
    def launcherPerformOTGSDir(self, configName):
        return ( self.launcherOTGSDir + configName + '/performOTGS/' )

    def fileProcessesPerformOTGS(self, configName):
        return ( self.launcherPerformOTGSDir(configName) + 'processesPerformOTGS.dat' )

    def fileLogPerformOTGS(self, configName):
        return ( self.launcherPerformOTGSDir(configName) + 'logPerformOTGS' )

    def fileNodesPerformOTGS(self, configName):
        return ( self.launcherPerformOTGSDir(configName) + 'nodesPerformOTGS.dat' )

    def pythonLauncherPerformOTGS(self, configName):
        return ( self.launcherPerformOTGSDir(configName) + 'performOTGS.py' )

    def bashLauncherPerformOTGS(self, configName):
        return ( self.launcherPerformOTGSDir(configName) + 'performOTGS.sh' )

    def performOTGSFieldSpeciesDir(self, AOG, field, LOL, species, TS):
        return ( self.OTGSDir + AOG + field.name + '/' + LOL + '/' + species + '/' + TS + '/' ) 

    def performOTGSP0P1FieldSpeciesDir(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.performOTGSFieldSpeciesDir(AOG, field, LOL, species, TS) + str(p0) + '-' + str(p1) + '/' + configName + '/' )

    def configFilePerformOTGSP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.performOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + configName + '.cfg' )

    def resultsFileOTGSP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.performOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'result.bin' )

    def TmapFileOTGSP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.performOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'Tmap.npy' )    

    def mergedResultsFileOTGSFieldSpecies(self, configName, AOG, field, LOL, species, TS):
        return ( self.performOTGSFieldSpeciesDir(AOG, field, LOL, species, TS) + 'results_'+configName )

    #_________________________

    def applyOTGSFieldSpeciesDir(self, AOG, field, LOL, species, TS):
        return ( self.applyOTGSDir + AOG + field.name + '/' + LOL + '/' + species + '/' + TS + '/' )

    def applyOTGSP0P1FieldSpeciesDir(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.applyOTGSFieldSpeciesDir(AOG, field, LOL, species, TS) + str(p0) + '-' + str(p1) + '/' + configName + '/' )

    def applyOTGSForwardP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.applyOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'forwardTransport.npy' )

    def applyOTGSBackwardP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.applyOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'backwardTransport.npy' )

    #_________________________

    def launcherPlotOT2DDir(self, configName):
        return ( self.launcherOT2DDir + configName + '/plotOT2D/' )
    
    def fileProcessesPlotOT2D(self, configName):
        return ( self.launcherPlotOT2DDir(configName) + 'processesPlotOT2D.dat' )

    def fileLogPlotOT2D(self, configName):
        return ( self.launcherPlotOT2DDir(configName) + 'logPlotOT2D' )

    def fileNodesPlotOT2D(self, configName):
        return ( self.launcherPlotOT2DDir(configName) + 'nodesPlotOT2D.dat' )

    def pythonLauncherPlotOT2D(self, configName):
        return ( self.launcherPlotOT2DDir(configName) + 'plotOT2D.py' )

    def bashLauncherPlotOT2D(self, configName):
        return ( self.launcherPlotOT2DDir(configName) + 'plotOT2D.sh' )

    def plotOT2DFieldSpeciesDir(self, AOG, field, LOL, species):
        return ( self.OT2DfigDir + AOG + field.name + '/' + LOL + '/' + species + '/' )

    def plotOT2DP0P1FieldSpeciesDir(self, configName, p0, p1, AOG, field, LOL, species):
        return ( self.plotOT2DFieldSpeciesDir(AOG, field, LOL, species) + str(p0) + '-' + str(p1) + '/' + configName + '/' )

    def configFilePlotOT2DP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species):
        return ( self.plotOT2DP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species) + 'plotting_' + configName + '.cfg' )

    #_________________________

    def launcherPlotOTGSDir(self, configName):
        return ( self.launcherOTGSDir + configName + '/plotOTGS/' )
    
    def fileProcessesPlotOTGS(self, configName):
        return ( self.launcherPlotOTGSDir(configName) + 'processesPlotOTGS.dat' )

    def fileLogPlotOTGS(self, configName):
        return ( self.launcherPlotOTGSDir(configName) + 'logPlotOTGS' )

    def fileNodesPlotOTGS(self, configName):
        return ( self.launcherPlotOTGSDir(configName) + 'nodesPlotOTGS.dat' )

    def pythonLauncherPlotOTGS(self, configName):
        return ( self.launcherPlotOTGSDir(configName) + 'plotOTGS.py' )

    def bashLauncherPlotOTGS(self, configName):
        return ( self.launcherPlotOTGSDir(configName) + 'plotOTGS.sh' )

    def plotOTGSFieldSpeciesDir(self, AOG, field, LOL, species, TS):
        return ( self.OTGSfigDir + AOG + field.name + '/' + LOL + '/' + species + '/' + TS + '/' )

    def plotOTGSP0P1FieldSpeciesDir(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.plotOTGSFieldSpeciesDir(AOG, field, LOL, species, TS) + str(p0) + '-' + str(p1) + '/' + configName + '/' )

    def configFilePlotOTGSP0P1FieldSpecies(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.plotOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS) + 'plotting_' + configName + '.cfg' )

    #_________________________

    def plotApplyGSTransportFieldSpeciesDir(self, AOG, field, LOL, species, TS):
        return ( self.applyGSTransportfigDir + AOG + field.name + '/' + LOL + '/' + species + '/' + TS + '/' )

    def plotApplyGSTransportP0P1FieldSpeciesDir(self, configName, p0, p1, AOG, field, LOL, species, TS):
        return ( self.plotApplyGSTransportFieldSpeciesDir(AOG, field, LOL, species, TS) + str(p0) + '-' + str(p1) + '/' + configName + '/' )

    #_________________________

    def makeProcLabelSuffixListList(self, AOO='all', addSimLabel=True):
        
        if AOO == 'all':
        
            procListList      = [self.procList]
            suffixFigNameList = ['allsim']

            if addSimLabel:
                labelListList = [self.labelList]
            else:
                labelList     = []
                for proc in self.procList:
                    labelList.append('')
                labelListList = [labelList]

        elif AOO == 'one':

            procListList      = []
            labelListList     = []
            suffixFigNameList = []

            for (proc, label) in zip(self.procList, self.labelList):
                procListList.append([proc])
                suffixFigNameList.append(label)
                
                if addSimLabel:
                    labelListList.append([label])
                else:
                    labelListList.append([''])

        return (procListList, labelListList, suffixFigNameList)

    #_________________________

    def fieldLOLList(self, AOG, field=None, LOL=None):

        if field is None:
            fieldList = self.fieldList[AOG]
        else:
            fieldList = []
            for f in self.fieldList[AOG]:
                if field == f.name:
                    fieldList.append(f)
                    break

        if LOL is None:
            LOLList   = LinOrLog()
        else:
            LOLList   = [LOL]

        return (fieldList, LOLList)

    #_________________________

    def fieldLOLTSList(self, AOG, field=None, LOL=None, TS=None):

        (fieldList, LOLList) = self.fieldLOLList(AOG, field, LOL)
        if TS is None:
            TSList = ThresholdNoThreshold()
        else:
            TSList = [TS]

        return (fieldList, LOLList, TSList)

#__________________________________________________
