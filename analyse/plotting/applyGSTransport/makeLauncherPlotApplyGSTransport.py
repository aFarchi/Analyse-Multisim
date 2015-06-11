#____________________________________
# makeLauncherPlotApplyGSTransport.py
#____________________________________

from itertools                                      import product

from plotTransportConfiguration                     import PlotTransportConfiguration
from ...utils.analyse.io.navigate                   import *
from ...utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ...utils.io.write                              import createDirectories
from ...utils.io.writeLaunchers                     import writeDefaultPythonLauncher
from ...utils.io.writeLaunchers                     import writeDefaultBashLauncher
from ...utils.io.writeLaunchers                     import writeDefaultNodesFile

#__________________________________________________

def makeLauncherPlotApplyGSTransport(configFile, availableProc=None):

    config    = PlotTransportConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPlotApplyGSTransportFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherPlotApplyGSTransportFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherPlotApplyGSTransportFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Plotting apply GS transport'
    args['$logFile$']       = simOutput.launcherPlotApplyGSTransportFiles['log']
    args['$nodesFile$']     = simOutput.launcherPlotApplyGSTransportFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherPlotApplyGSTransportFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherPlotApplyGSTransportFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherPlotApplyGSTransportFiles['nodes'])
    
    f = open(simOutput.launcherPlotApplyGSTransportFiles['processes'], 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'PARLLELIZE'  + '\t' +
            'AOG'         + '\t' +
            'SPECIES'     + '\t' +
            'FIELD'       + '\t' +
            'LOL'         + '\t' +
            'TS'          + '\t' +
            'CONFIG_NAME' + '\n' )

    dirsToCreate = []
    
    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:

            for (field,
                 LOL,
                 TS,
                 configName) in product(simOutput.fieldList[AOG],
                                        LinOrLog(),
                                        ThresholdNoThreshold(),
                                        config.OTGS_configurationNames):
                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):
                        dirsToCreate.append(simOutput.plotApplyGSTransportP0P1FieldSpeciesDir(configName, 
                                                                                              p0, 
                                                                                              p1, 
                                                                                              AOG, 
                                                                                              field, 
                                                                                              LOL, 
                                                                                              species, 
                                                                                              TS))

            if config.plotApplyGSTransport_parallelize == 'less':
                f.write('plotApplyGSTransport'                                + '\t' +
                        simOutput.launcherPlotApplyGSTransportFiles['config'] + '\t' +
                        'less'                                                + '\t' +
                        AOG                                                   + '\t' +
                        species                                               + '\t' +
                        'None'                                                + '\t' +
                        'None'                                                + '\t' +
                        'None'                                                + '\t' +
                        'None'                                                + '\n' )

            elif config.plotApplyGSTransport_parallelize == 'more':

                for (field, 
                     LOL, 
                     TS, 
                     configName) in product(simOutput.fieldList[AOG], 
                                            LinOrLog(), 
                                            ThresholdNoThreshold(), 
                                            config.OTGS_configurationNames):

                    f.write('plotApplyGSTransport'                                + '\t' +
                            simOutput.launcherPlotApplyGSTransportFiles['config'] + '\t' +
                            'more'                                                + '\t' +
                            AOG                                                   + '\t' +
                            species                                               + '\t' +
                            field.name                                            + '\t' +
                            LOL                                                   + '\t' +
                            TS                                                    + '\t' +
                            configName                                            + '\n' )

    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherPlotApplyGSTransportFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherPlotApplyGSTransportFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherPlotApplyGSTransportFiles['processes']+' ...')
    print('Written '+simOutput.launcherPlotApplyGSTransportFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
