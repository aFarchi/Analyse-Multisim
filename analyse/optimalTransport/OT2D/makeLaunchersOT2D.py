#_____________________
# makeLaunchersOT2D.py
#_____________________

from itertools                                            import product

from OT2DConfiguration                                    import OT2DConfiguration
from ...utils.analyse.io.navigate                         import *
from ...utils.analyse.simulation.simulationsOutput        import buildSimulationsOutput
from ...utils.io.write                                    import createDirectories
from ...utils.io.writeLaunchers                           import writeDefaultPythonLauncher
from ...utils.io.writeLaunchers                           import writeDefaultBashLauncher
from ...utils.io.writeLaunchers                           import writeDefaultNodesFile
from ...utils.io.writeOTConfig                            import writeDefaultConfigOT2D
from ...utils.io.writeOTConfig                            import writeDefaultPlottingConfigOT2DAllConfig
from ...utils.io.writeOTConfig                            import writeDefaultPlottingConfigOT2D
from ...utils.analyse.timeSelection.defaultTimeResolution import minTimeRes
from ...utils.analyse.timeSelection.defaultTimeResolution import maxTimeRes

#__________________________________________________

def makeLauncherInterpolateIntoOTResolution(configFile):
    
    config    = OT2DConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherInterpolateIntoOT2DResolutionDir], config.printIO)
    config.writeConfig(simOutput.configFileInterpolateIntoOT2DResolutionDir)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesInterpolateIntoOT2DResolutionDir
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'

    args['$logFile$']       = simOutput.fileLogInterpolateIntoOT2DResolutionDir
    args['$nodesFile$']     = simOutput.fileNodesInterpolateIntoOT2DResolutionDir

    writeDefaultPythonLauncher(simOutput.pythonLauncherInterpolateIntoOT2DResolutionDir, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherInterpolateIntoOT2DResolutionDir, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesInterpolateIntoOT2DResolutionDir)
    
    f = open(simOutput.fileProcessesInterpolateIntoOT2DResolutionDir, 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'RUN_AOO'     + '\t' +
            'AOG'         + '\t' +
            'GOR'         + '\t' +
            'SPECIES'     + '\n' )

    dirsToCreate = []
    for (AOG, LOL) in product(AirOrGround(), LinOrLog()):
        for (field, proc) in product(simOutput.fieldList[AOG], simOutput.procList):
            dirsToCreate.append(simOutput.procPreprocessedFieldOTResolutionDir(proc, AOG, field, LOL))

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:
            f.write('interpolateIntoOT2DResolutionDir'                   + '\t' +
                    simOutput.configFileInterpolateIntoOT2DResolutionDir + '\t' +
                    'one'                                                + '\t' +
                    AOG                                                  + '\t' +
                    GOR                                                  + '\t' +
                    species                                              + '\n' )
    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.pythonLauncherInterpolateIntoOT2DResolutionDir+' ...')
    print('Written '+simOutput.bashLauncherInterpolateIntoOT2DResolutionDir+' ...')
    print('Written '+simOutput.fileProcessesInterpolateIntoOT2DResolutionDir+' ...')
    print('Written '+simOutput.fileNodesInterpolateIntoOT2DResolutionDir+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPerformOT2D(configFile):

    config    = OT2DConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    if config.OT2D_timeResFunction == 'min':
        timeResFunction = minTimeRes
    elif config.OT2D_timeResFunction == 'max':
        timeResFunction = maxTimeRes

    for configName in config.OT2D_configurationName:

        createDirectories([simOutput.launcherPerformOT2DDir(configName)], config.printIO)

        args                    = {}
        args['$fileProcesses$'] = simOutput.fileProcessesPerformOT2D(configName)
        args['$launcher$']      = simOutput.modulePath.OT2DLauncher
        args['$interpretor$']   = 'python'
        args['$startString$']   = 'Starting OT2D ...'
        
        args['$logFile$']       = simOutput.fileLogPerformOT2D(configName)
        args['$nodesFile$']     = simOutput.fileNodesPerformOT2D(configName)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPerformOT2D(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPerformOT2D(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPerformOT2D(configName))
        
        args = {}
        args['$EPSILON$']    = str(config.EPSILON)
    
        f = open(simOutput.fileProcessesPerformOT2D(configName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        directory = simOutput.performOT2DP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)
                        createDirectories([directory], config.printIO)
                        
                        M = config.OT2D_shape[field.axes[0]]
                        N = config.OT2D_shape[field.axes[1]]

                        args['$outputDir$'] = directory
                        args['$M$']         = str(M)
                        args['$N$']         = str(N)
                        args['$P$']         = str(timeResFunction(M, N))

                        args['$filef0$']    = simOutput.fileProcPreprocessedField(simOutput.procList[p0], AOG, field, LOL, species)
                        args['$filef1$']    = simOutput.fileProcPreprocessedField(simOutput.procList[p1], AOG, field, LOL, species)

                        writeDefaultConfigOT2D(simOutput.configFilePerformOT2DP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species), 
                                               args, config.OT2D_algorithmParametersFiles[configName])

                        f.write(simOutput.configFilePerformOT2DP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPerformOT2D(configName)+' ...')
        print('Written '+simOutput.bashLauncherPerformOT2D(configName)+' ...')
        print('Written '+simOutput.fileProcessesPerformOT2D(configName)+' ...')
        print('Written '+simOutput.fileNodesPerformOT2D(configName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPlotOT2DSingleConfig(configFile):

    config    = OT2DConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    for configName in config.OT2D_configurationName:

        createDirectories([simOutput.launcherPlotOT2DDir(configName)], config.printIO)

        args                    = {}
        args['$fileProcesses$'] = simOutput.fileProcessesPlotOT2D(configName)
        args['$launcher$']      = simOutput.modulePath.OT2DLauncherPlotting
        args['$interpretor$']   = 'python'
        args['$startString$']   = 'Plotting OT2D ...'
        
        args['$logFile$']       = simOutput.fileLogPlotOT2D(configName)
        args['$nodesFile$']     = simOutput.fileNodesPlotOT2D(configName)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPlotOT2D(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPlotOT2D(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPlotOT2D(configName))
        
        args = {}
        args['$EPSILON$']     = str(config.EPSILON)
        args['singleOrMulti'] = str(0)

        f = open(simOutput.fileProcessesPlotOT2D(configName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        outputDir = simOutput.performOT2DP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)
                        figDir    = simOutput.plotOT2DP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)
                        label     = str(p0) + '-' + str(p1) + ', ' + configName

                        createDirectories([figDir], config.printIO)
                        args['$figDir$']    = figDir 
                        args['$outputDir$'] = outputDir
                        args['$label$']     = label

                        writeDefaultPlottingConfigOT2D(simOutput.configFilePlotOT2DP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species), 
                                                       args, config.OT2D_plottingParametersFiles[configName])

                        f.write(simOutput.configFilePlotOT2DP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPlotOT2D(configName)+' ...')
        print('Written '+simOutput.bashLauncherPlotOT2D(configName)+' ...')
        print('Written '+simOutput.fileProcessesPlotOT2D(configName)+' ...')
        print('Written '+simOutput.fileNodesPlotOT2D(configName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPlotOT2DMultiConfig(configFile):

    config     = OT2DConfiguration(configFile)
    simOutput  = buildSimulationsOutput(config)
    configName = 'allConfigs'

    createDirectories([simOutput.launcherPlotOT2DDir(configName)], config.printIO)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesPlotOT2D(configName)
    args['$launcher$']      = simOutput.modulePath.OT2DLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Plotting OT2D ...'
        
    args['$logFile$']       = simOutput.fileLogPlotOT2D(configName)
    args['$nodesFile$']     = simOutput.fileNodesPlotOT2D(configName)

    writeDefaultPythonLauncher(simOutput.pythonLauncherPlotOT2D(configName), args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherPlotOT2D(configName), args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesPlotOT2D(configName))
        
    args = {}
    args['$EPSILON$']     = str(config.EPSILON)
    args['singleOrMulti'] = str(1)

    f = open(simOutput.fileProcessesPlotOT2D(configName), 'w')
    f.write('CONFIG_FILE' + '\t' +
            'PRINT_IO'    + '\n' )

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

            for p1 in xrange(len(simOutput.procList)):
                for p0 in xrange(p1):

                    outputDirList = []
                    labelList     = []
                    for cName in config.OT2D_configurationName:
                        outputDirList.append(simOutput.performOT2DP0P1FieldSpeciesDir(cName, p0, p1, AOG, field, LOL, species))
                        labelList.append(cName)

                    figDir = simOutput.plotOT2DP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)

                    createDirectories([figDir], config.printIO)
                    args['$figDir$'] = figDir 

                    writeDefaultPlottingConfigOT2DAllConfig(simOutput.configFilePlotOT2DP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species), 
                                                            args, outputDirList, labelList, config.OT2D_plottingParametersFileAllConfig)

                    f.write(simOutput.configFilePlotOT2DP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species)+'\t')
                    f.write(str(config.printIO)+'\n')

    f.close()

    print('Written '+simOutput.pythonLauncherPlotOT2D(configName)+' ...')
    print('Written '+simOutput.bashLauncherPlotOT2D(configName)+' ...')
    print('Written '+simOutput.fileProcessesPlotOT2D(configName)+' ...')
    print('Written '+simOutput.fileNodesPlotOT2D(configName)+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

