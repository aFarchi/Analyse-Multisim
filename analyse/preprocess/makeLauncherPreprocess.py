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

def makeLauncherPreprocessRawData(configFile, availableProc=None):

    config    = PreprocessConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPreprocessRawDataFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherPreprocessRawDataFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherPreprocessRawDataFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'
    args['$logFile$']       = simOutput.launcherPreprocessRawDataFiles['log']
    args['$nodesFile$']     = simOutput.launcherPreprocessRawDataFiles['nodes']

    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherPreprocessRawDataFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherPreprocessRawDataFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherPreprocessRawDataFiles['nodes'])

    f = open(simOutput.launcherPreprocessRawDataFiles['processes'], 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
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
            f.write('preprocessRawData'                                + '\t' +
                    simOutput.launcherPreprocessRawDataFiles['config'] + '\t' +
                    AOG                                                + '\t' +
                    GOR                                                + '\t' +
                    species                                            + '\n' )
    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherPreprocessRawDataFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherPreprocessRawDataFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherPreprocessRawDataFiles['processes']+' ...')
    print('Written '+simOutput.launcherPreprocessRawDataFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
