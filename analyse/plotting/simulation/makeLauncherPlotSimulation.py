#______________________________
# makeLauncherPlotSimulation.py
#______________________________

from itertools                                     import product

from plotSimulationConfiguration                   import PlotSimulationConfiguration
from ...utils.analyse.io.navigate                  import *
from ...utils.analyse.simulation.simulationsOutput import buildSimulationsOutput
from ...utils.io.write                             import createDirectories
from ...utils.io.writeLaunchers                    import writeDefaultPythonLauncher
from ...utils.io.writeLaunchers                    import writeDefaultBashLauncher
from ...utils.io.writeLaunchers                    import writeDefaultNodesFile

#__________________________________________________

def makeLauncherPlotSimulation(configFile, availableProc=None):

    config    = PlotSimulationConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPlotSimulationFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherPlotSimulationFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherPlotSimulationFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'
    args['$logFile$']       = simOutput.launcherPlotSimulationFiles['log']
    args['$nodesFile$']     = simOutput.launcherPlotSimulationFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherPlotSimulationFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherPlotSimulationFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherPlotSimulationFiles['nodes'])
    
    f = open(simOutput.launcherPlotSimulationFiles['processes'], 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'PARLLELIZE'  + '\t' +
            'AOG'         + '\t' +
            'GOR'         + '\t' +
            'SPECIES'     + '\t' +
            'FIELD'       + '\t' +
            'LOL'         + '\n' )

    dirsToCreate = []
    
    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:

            for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                dirsToCreate.append(simOutput.simOutputFieldFigDir(AOG, field, LOL, species))

            if config.plotSimulationsField_parallelize == 'less':
                f.write('plotSimulation'                                + '\t' +
                        simOutput.launcherPlotSimulationFiles['config'] + '\t' +
                        'less'                                          + '\t' +
                        AOG                                             + '\t' +
                        GOR                                             + '\t' +
                        species                                         + '\t' +
                        'None'                                          + '\t' +
                        'None'                                          + '\n' )

            elif config.plotSimulationsField_parallelize == 'more':

                for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                    f.write('plotSimulation'                                + '\t' +
                            simOutput.launcherPlotSimulationFiles['config'] + '\t' +
                            'less'                                          + '\t' +
                            AOG                                             + '\t' +
                            GOR                                             + '\t' +
                            species                                         + '\t' +
                            field.name                                      + '\t' +
                            LOL                                             + '\n' )

    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherPlotSimulationFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherPlotSimulationFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherPlotSimulationFiles['processes']+' ...')
    print('Written '+simOutput.launcherPlotSimulationFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
