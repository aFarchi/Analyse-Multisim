#__________________________
# makeLauncherPreprocess.py
#__________________________

from itertools import product

from ..utils.io.write                   import createDirectories
from ..utils.io.writeLaunchers          import writeDefaultPythonLauncher
from ..utils.io.writeLaunchers          import writeDefaultBashLauncher
from ..utils.io.writeLaunchers          import writeDefaultNodesFile
from ..utils.analyse.simulationsOutput  import buildSimulationsOutput
from createDirectoriesPreprocessRawData import createDirectoriesPreprocessRawData
from preprocessConfiguration            import PreprocessConfiguration

#__________________________________________________

def makeLauncherPreprocessRawDataForAllSpecies(configFile):

    preprocessConfig = PreprocessConfiguration(configFile)
    simOutput        = buildSimulationsOutput(preprocessConfig)

    createDirectoriesPreprocessRawData(simOutput, preprocessConfig.printIO)
    createDirectories([simOutput.launcherPreprocessRawDataDir], preprocessConfig.printIO)
    preprocessConfig.writeConfig(simOutput.configFilePreprocessRawData)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesPreprocessRawData
    args['$launcher$']      = simOutput.modulePath.module.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'

    args['$logFile$']       = simOutput.fileLogPreprocessRawData
    args['$nodesFile$']     = simOutput.fileNodesPreprocessRawData

    writeDefaultPythonLauncher(simOutput.pythonLauncherPreprocessRawData, args, makeExe=True, printIO=preprocessConfig.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherPreprocessRawData, args, makeExe=True, printIO=preprocessConfig.printIO)
    writeDefaultNodesFile(simOutput.fileNodesPreprocessRawData)

    f     = open(simOutput.fileProcessesPreprocessRawData, 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'RUN_AOO'     + '\t' +
            'AOG'         + '\t' +
            'GOR'         + '\t' +
            'SPECIES'     + '\n' )

    for (AOG, GOR) in product(AirOrGround, GazOrRadios):
        for species in simOutput.simConfig.speciesList[GOR]:
            f.write('preprocessRawData'                      + '\t' +
                    simOutput.fileProcessesPreprocessRawData + '\t' +
                    'one'                                    + '\t' +
                    AOG                                      + '\t' +
                    GOR                                      + '\t' +
                    species                                  + '\n' )
    f.close()
    
    print('Written '+simOutput.pythonLauncherPreprocessRawData+' ...')
    print('Written '+simOutput.bashLauncherPreprocessRawData+' ...')
    print('Written '+simOutput.fileProcessesPreprocessRawData+' ...')
    print('Written '+simOutput.fileNodesPreprocessRawData+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
