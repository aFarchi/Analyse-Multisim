#______________________________
# makeLauncherPlotSimulation.py
#______________________________

from itertools                                      import product

from plotSimulationConfiguration                    import PlotSimulationConfiguration
from ...utils.analyse.io.navigate                   import *
from ...utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ...utils.io.write                              import createDirectories
from ...utils.io.writeLaunchers                     import writeDefaultPythonLauncher
from ...utils.io.writeLaunchers                     import writeDefaultBashLauncher
from ...utils.io.writeLaunchers                     import writeDefaultNodesFile

#__________________________________________________

def makeLauncherPlotSimulation(configFile):

    config    = PlotSimulationConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPlotSimulationDir], config.printIO)
    config.writeConfig(simOutput.configFilePlotSimulation)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesPlotSimulation
    args['$launcher$']      = simOutput.modulePath.moduleLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'

    args['$logFile$']       = simOutput.fileLogPlotSimulation
    args['$nodesFile$']     = simOutput.fileNodesPlotSimulation

    writeDefaultPythonLauncher(simOutput.pythonLauncherPlotSimulation, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherPlotSimulation, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesPlotSimulation)
    
    f = open(simOutput.fileProcessesPlotSimulation, 'w')
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
                f.write('plotSimulation'                   + '\t' +
                        simOutput.configFilePlotSimulation + '\t' +
                        'less'                             + '\t' +
                        AOG                                + '\t' +
                        GOR                                + '\t' +
                        species                            + '\t' +
                        'None'                             + '\t' +
                        'None'                             + '\n' )

            elif config.plotSimulationsField_parallelize == 'more':

                for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                    f.write('plotSimulation'                   + '\t' +
                            simOutput.configFilePlotSimulation + '\t' +
                            'less'                             + '\t' +
                            AOG                                + '\t' +
                            GOR                                + '\t' +
                            species                            + '\t' +
                            field.name                         + '\t' +
                            LOL                                + '\n' )

    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.pythonLauncherPlotSimulation+' ...')
    print('Written '+simOutput.bashLauncherPlotSimulation+' ...')
    print('Written '+simOutput.fileProcessesPlotSimulation+' ...')
    print('Written '+simOutput.fileNodesPlotSimulation+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
