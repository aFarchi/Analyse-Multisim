#__________________________________
# makeLauncherStatisticalAnalyse.py
#__________________________________

from itertools                                    import product

from statisticalAnalyseConfiguration              import StatisticalAnalyseConfiguration
from ..utils.analyse.io.navigate                  import *
from ..utils.analyse.simulation.simulationsOutput import buildSimulationsOutput
from ..utils.io.write                             import createDirectories
from ..utils.io.writeLaunchers                    import writeDefaultPythonLauncher
from ..utils.io.writeLaunchers                    import writeDefaultBashLauncher
from ..utils.io.writeLaunchers                    import writeDefaultNodesFile

#__________________________________________________

def makeLauncherStatisticalAnalyse(configFile, availableProc=None):

    config    = StatisticalAnalyseConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherStatisticalAnalyseFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherStatisticalAnalyseFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherStatisticalAnalyseFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Starting statistical analyse ...'
    args['$logFile$']       = simOutput.launcherStatisticalAnalyseFiles['log']
    args['$nodesFile$']     = simOutput.launcherStatisticalAnalyseFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherStatisticalAnalyseFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherStatisticalAnalyseFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherStatisticalAnalyseFiles['nodes'])

    f = open(simOutput.launcherStatisticalAnalyseFiles['processes'], 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'PARALLELIZE' + '\t' +
            'AOG'         + '\t' +
            'SPECIES'     + '\t' +
            'FIELD'       + '\t' +
            'LOL'         + '\n' )

    dirsToCreate = []

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:

            for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                dirsToCreate.append(simOutput.analyseFieldSeciesDir(AOG, field, LOL, species))

            if config.statisticalAnalyse_parallelize == 'less':
                f.write('performStatisticalAnalyse'                         + '\t' +
                        simOutput.launcherStatisticalAnalyseFiles['config'] + '\t' +
                        'less'                                              + '\t' +
                        AOG                                                 + '\t' +
                        species                                             + '\t' +
                        'None'                                              + '\t' +
                        'None'                                              + '\n' )

            elif config.statisticalAnalyse_parallelize == 'more':

                for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                    f.write('performStatisticalAnalyse'                         + '\t' +
                            simOutput.launcherStatisticalAnalyseFiles['config'] + '\t' +
                            'more'                                              + '\t' +
                            AOG                                                 + '\t' +
                            species                                             + '\t' +
                            field.name                                          + '\t' +
                            LOL                                                 + '\n' )
            
    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherStatisticalAnalyseFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherStatisticalAnalyseFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherStatisticalAnalyseFiles['processes']+' ...')
    print('Written '+simOutput.launcherStatisticalAnalyseFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
