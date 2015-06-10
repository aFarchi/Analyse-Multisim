#__________________________
# makeLauncherPlotFields.py
#__________________________

from itertools                                      import product

from plotFieldsConfiguration                        import PlotFieldsConfiguration
from ...utils.analyse.io.navigate                   import *
from ...utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ...utils.io.write                              import createDirectories
from ...utils.io.writeLaunchers                     import writeDefaultPythonLauncher
from ...utils.io.writeLaunchers                     import writeDefaultBashLauncher
from ...utils.io.writeLaunchers                     import writeDefaultNodesFile

#__________________________________________________

def makeLauncherPlotFields(configFile, availableProc=None):

    config    = PlotFieldsConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPlotFieldFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherPlotFieldFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherPlotFieldFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'
    args['$logFile$']       = simOutput.launcherPlotFieldFiles['log']
    args['$nodesFile$']     = simOutput.launcherPlotFieldFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherPlotFieldFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherPlotFieldFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherPlotFieldFiles['nodes'])
    
    f = open(simOutput.launcherPlotFieldFiles['processes'], 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'PARLLELIZE'  + '\t' +
            'AOG'         + '\t' +
            'SPECIES'     + '\t' +
            'FIELD'       + '\t' +
            'LOL'         + '\n' )

    dirsToCreate = []
    
    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:

            for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                dirsToCreate.append(simOutput.fieldFigDir(AOG, field, LOL, species))
                dirsToCreate.append(simOutput.fieldAttachGrayScaleFigDir(AOG, field, LOL, species))

            if config.plotFields_parallelize == 'less':
                f.write('plotFields'                               + '\t' +
                        simOutput.launcherPlotFieldFiles['config'] + '\t' +
                        'less'                                     + '\t' +
                        AOG                                        + '\t' +
                        species                                    + '\t' +
                        'None'                                     + '\t' +
                        'None'                                     + '\n' )

            elif config.plotFields_parallelize == 'more':

                for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                    f.write('plotFields'                               + '\t' +
                            simOutput.launcherPlotFieldFiles['config'] + '\t' +
                            'less'                                     + '\t' +
                            AOG                                        + '\t' +
                            species                                    + '\t' +
                            field.name                                 + '\t' +
                            LOL                                        + '\n' )

    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherPlotFieldFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherPlotFieldFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherPlotFieldFiles['processes']+' ...')
    print('Written '+simOutput.launcherPlotFieldFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
