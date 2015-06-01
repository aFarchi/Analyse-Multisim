#__________________________
# makeLauncherPreprocess.py
#__________________________

from itertools                                     import product

from preprocessConfiguration                       import PreprocessConfiguration
from ..utils.analyse.io.navigate                   import *
from ..utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ..utils.io.write                              import createDirectories
from ..utils.io.writeLaunchers                     import writeDefaultPythonLauncher
from ..utils.io.writeLaunchers                     import writeDefaultBashLauncher
from ..utils.io.writeLaunchers                     import writeDefaultNodesFile

#__________________________________________________

def makeLauncherPreprocessRawDataForAllSpecies(configFile):

    config    = PreprocessConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPreprocessRawDataDir], config.printIO)
    config.writeConfig(simOutput.configFilePreprocessRawData)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesPreprocessRawData
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'

    args['$logFile$']       = simOutput.fileLogPreprocessRawData
    args['$nodesFile$']     = simOutput.fileNodesPreprocessRawData

    writeDefaultPythonLauncher(simOutput.pythonLauncherPreprocessRawData, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherPreprocessRawData, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesPreprocessRawData)

    f = open(simOutput.fileProcessesPreprocessRawData, 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'RUN_AOO'     + '\t' +
            'AOG'         + '\t' +
            'GOR'         + '\t' +
            'SPECIES'     + '\n' )

    dirsToCreate = []
    for (AOG, LOL) in product(AirOrGround(), LinOrLog()):
        for field in simOutput.fieldList[AOG]:
            dirsToCreate.append(simOutput.scalingFieldDir(AOG, field, LOL))
            for proc in simOutput.procList:
                dirsToCreate.append(simOutput.procPreprocessedFieldDir(proc, AOG, field, LOL))


    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:
            f.write('preprocessRawData'                   + '\t' +
                    simOutput.configFilePreprocessRawData + '\t' +
                    'one'                                 + '\t' +
                    AOG                                   + '\t' +
                    GOR                                   + '\t' +
                    species                               + '\n' )
    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.pythonLauncherPreprocessRawData+' ...')
    print('Written '+simOutput.bashLauncherPreprocessRawData+' ...')
    print('Written '+simOutput.fileProcessesPreprocessRawData+' ...')
    print('Written '+simOutput.fileNodesPreprocessRawData+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
