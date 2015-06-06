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

def makeLauncherPlotFields(configFile):

    config    = PlotFieldsConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherPlotFieldsDir], config.printIO)
    config.writeConfig(simOutput.configFilePlotFields)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesPlotFields
    args['$launcher$']      = simOutput.modulePath.moduleLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'

    args['$logFile$']       = simOutput.fileLogPlotFields
    args['$nodesFile$']     = simOutput.fileNodesPlotFields

    writeDefaultPythonLauncher(simOutput.pythonLauncherPlotFields, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherPlotFields, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesPlotFields)
    
    f = open(simOutput.fileProcessesPlotFields, 'w')
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
                dirsToCreate.append(simOutput.fieldFigDir(AOG, field, LOL, species))
                dirsToCreate.append(simOutput.fieldAttachGrayScaleFigDir(AOG, field, LOL, species))

            if config.plotFields_parallelize == 'less':
                f.write('plotFields'                   + '\t' +
                        simOutput.configFilePlotFields + '\t' +
                        'less'                         + '\t' +
                        AOG                            + '\t' +
                        GOR                            + '\t' +
                        species                        + '\t' +
                        'None'                         + '\t' +
                        'None'                         + '\n' )

            elif config.plotFields_parallelize == 'more':

                for (field, LOL) in product(simOutput.fieldList[AOG], LinOrLog()):
                    f.write('plotFields'                   + '\t' +
                            simOutput.configFilePlotFields + '\t' +
                            'less'                         + '\t' +
                            AOG                            + '\t' +
                            GOR                            + '\t' +
                            species                        + '\t' +
                            field.name                     + '\t' +
                            LOL                            + '\n' )

    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.pythonLauncherPlotFields+' ...')
    print('Written '+simOutput.bashLauncherPlotFields+' ...')
    print('Written '+simOutput.fileProcessesPlotFields+' ...')
    print('Written '+simOutput.fileNodesPlotFields+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
