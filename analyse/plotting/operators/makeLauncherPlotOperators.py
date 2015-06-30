#__________________________
# makeLauncherPlotFields.py
#__________________________

from itertools                                      import product

from plotOperatorsConfiguration                     import PlotOperatorsConfiguration
from ...utils.analyse.io.navigate                   import *
from ...utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ...utils.io.write                              import createDirectories
from ...utils.io.writeLaunchers                     import writeDefaultPythonLauncher
from ...utils.io.writeLaunchers                     import writeDefaultBashLauncher
from ...utils.io.writeLaunchers                     import writeDefaultNodesFile

#__________________________________________________

def makeLauncherPlotOperators(configFile, availableProc=None):

    config    = PlotOperatorsConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPlotOperatorsFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherPlotOperatorsFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherPlotOperatorsFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'plotting operators'
    args['$logFile$']       = simOutput.launcherPlotOperatorsFiles['log']
    args['$nodesFile$']     = simOutput.launcherPlotOperatorsFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherPlotOperatorsFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherPlotOperatorsFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherPlotOperatorsFiles['nodes'])
    
    f = open(simOutput.launcherPlotOperatorsFiles['processes'], 'w')
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
                dirsToCreate.append(simOutput.plotOperatorsDir(AOG, field, LOL, species))

            if config.plotOperators_parallelize == 'less':
                f.write('plotOperators'                                + '\t' +
                        simOutput.launcherPlotOperatorsFiles['config'] + '\t' +
                        'less'                                         + '\t' +
                        AOG                                            + '\t' +
                        species                                        + '\t' +
                        'None'                                         + '\t' +
                        'None'                                         + '\n' )

            elif config.plotOperators_parallelize == 'more':

                for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                    f.write('plotOperators'                                + '\t' +
                            simOutput.launcherPlotOperatorsFiles['config'] + '\t' +
                            'more'                                         + '\t' +
                            AOG                                            + '\t' +
                            species                                        + '\t' +
                            field.name                                     + '\t' +
                            LOL                                            + '\n' )

    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherPlotOperatorsFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherPlotOperatorsFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherPlotOperatorsFiles['processes']+' ...')
    print('Written '+simOutput.launcherPlotOperatorsFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
