#_____________________
# makeLaunchersOTGS.py
#_____________________

from itertools                                            import product

from OTGSConfiguration                                    import OTFSConfiguration
from ...utils.analyse.io.navigate                         import *
from ...utils.analyse.simulation.simulationsOutput        import buildSimulationsOutput
from ...utils.io.write                                    import createDirectories
from ...utils.io.writeLaunchers                           import writeDefaultPythonLauncher
from ...utils.io.writeLaunchers                           import writeDefaultBashLauncher
from ...utils.io.writeLaunchers                           import writeDefaultNodesFile
from ...utils.io.writeOTConfig                            import writeDefaultConfigOTGS
from ...utils.io.writeOTConfig                            import writeDefaultPlottingConfigOTGSAllConfig
from ...utils.io.writeOTConfig                            import writeDefaultPlottingConfigOTGS
from ...utils.analyse.timeSelection.defaultTimeResolution import minTimeRes
from ...utils.analyse.timeSelection.defaultTimeResolution import maxTimeRes

#__________________________________________________

def makeLauncherInterpolateIntoOTGSResolution(configFile):
    
    config    = OTGSConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherInterpolateIntoOTGSResolutionDir], config.printIO)
    config.writeConfig(simOutput.configFileInterpolateIntoOTGSResolutionDir)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesInterpolateIntoOTGSResolutionDir
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'

    args['$logFile$']       = simOutput.fileLogInterpolateIntoOTGSResolutionDir
    args['$nodesFile$']     = simOutput.fileNodesInterpolateIntoOTGSResolutionDir

    writeDefaultPythonLauncher(simOutput.pythonLauncherInterpolateIntoOTGSResolutionDir, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherInterpolateIntoOTGSResolutionDir, args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesInterpolateIntoOTGSResolutionDir)
    
    f = open(simOutput.fileProcessesInterpolateIntoOTGSResolutionDir, 'w')
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
            f.write('interpolateIntoOTGSResolutionDir'                   + '\t' +
                    simOutput.configFileInterpolateIntoOTGSResolutionDir + '\t' +
                    'one'                                                + '\t' +
                    AOG                                                  + '\t' +
                    GOR                                                  + '\t' +
                    species                                              + '\n' )
    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.pythonLauncherInterpolateIntoOTGSResolutionDir+' ...')
    print('Written '+simOutput.bashLauncherInterpolateIntoOTGSResolutionDir+' ...')
    print('Written '+simOutput.fileProcessesInterpolateIntoOTGSResolutionDir+' ...')
    print('Written '+simOutput.fileNodesInterpolateIntoOTGSResolutionDir+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPerformOTGS(configFile):

    config    = OTGSConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    if config.OTGS_timeResFunction == 'min':
        timeResFunction = minTimeRes
    elif config.OTGS_timeResFunction == 'max':
        timeResFunction = maxTimeRes

    for configName in config.OTGS_configurationNames:

        createDirectories([simOutput.launcherPerformOTGSDir(configName)], config.printIO)

        args                    = {}
        args['$fileProcesses$'] = simOutput.fileProcessesPerformOTGS(configName)
        args['$launcher$']      = simOutput.modulePath.OT1DLauncher
        args['$interpretor$']   = 'python'
        args['$startString$']   = 'Starting OTGS ...'
        
        args['$logFile$']       = simOutput.fileLogPerformOTGS(configName)
        args['$nodesFile$']     = simOutput.fileNodesPerformOTGS(configName)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPerformOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPerformOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPerformOTGS(configName))
        
        args = {}
        args['$EPSILON$']    = str(config.EPSILON)
    
        f = open(simOutput.fileProcessesPerformOTGS(configName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        directory = simOutput.performOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)
                        createDirectories([directory], config.printIO)
                        
                        N = config.OTGS_resolution
                        
                        args['$outputDir$'] = directory
                        args['$N$']         = str(N)
                        args['$P$']         = str(N)

                        args['$filef0$']    = simOutput.fileProcPreprocessedFieldGSOTResolution(simOutput.procList[p0], AOG, field, LOL, species)
                        args['$filef1$']    = simOutput.fileProcPreprocessedFieldGSOTResolution(simOutput.procList[p1], AOG, field, LOL, species)

                        writeDefaultConfigOTGS(simOutput.configFilePerformOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species), 
                                               args, config.OTGS_algorithmParametersFiles[configName])

                        f.write(simOutput.configFilePerformOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPerformOTGS(configName)+' ...')
        print('Written '+simOutput.bashLauncherPerformOTGS(configName)+' ...')
        print('Written '+simOutput.fileProcessesPerformOTGS(configName)+' ...')
        print('Written '+simOutput.fileNodesPerformOTGS(configName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPlotOTGSSingleConfig(configFile):

    config    = OTGSConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    for configName in config.OTGS_configurationNames:

        createDirectories([simOutput.launcherPlotOTGSDir(configName)], config.printIO)

        args                    = {}
        args['$fileProcesses$'] = simOutput.fileProcessesPlotOTGS(configName)
        args['$launcher$']      = simOutput.modulePath.OT1DLauncherPlotting
        args['$interpretor$']   = 'python'
        args['$startString$']   = 'Plotting OTGS ...'
        
        args['$logFile$']       = simOutput.fileLogPlotOTGS(configName)
        args['$nodesFile$']     = simOutput.fileNodesPlotOTGS(configName)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPlotOTGS(configName))
        
        args = {}
        args['$EPSILON$']     = str(config.EPSILON)
        args['$singleOrMulti$'] = str(0)

        f = open(simOutput.fileProcessesPlotOTGS(configName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        outputDir = simOutput.performOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)
                        figDir    = simOutput.plotOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)
                        label     = str(p0) + '-' + str(p1) + ', ' + configName

                        createDirectories([figDir], config.printIO)
                        args['$figDir$']    = figDir 
                        args['$outputDir$'] = outputDir
                        args['$label$']     = label

                        writeDefaultPlottingConfigOTGS(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species), 
                                                       args, config.OTGS_plottingParametersFiles[configName])

                        f.write(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPlotOTGS(configName)+' ...')
        print('Written '+simOutput.bashLauncherPlotOTGS(configName)+' ...')
        print('Written '+simOutput.fileProcessesPlotOTGS(configName)+' ...')
        print('Written '+simOutput.fileNodesPlotOTGS(configName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPlotOTGSMultiConfig(configFile):

    config     = OTGSConfiguration(configFile)
    simOutput  = buildSimulationsOutput(config)
    configName = 'allConfigs'

    createDirectories([simOutput.launcherPlotOTGSDir(configName)], config.printIO)

    args                    = {}
    args['$fileProcesses$'] = simOutput.fileProcessesPlotOTGS(configName)
    args['$launcher$']      = simOutput.modulePath.OT1DLauncherPlotting
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Plotting OTGS ...'
        
    args['$logFile$']       = simOutput.fileLogPlotOTGS(configName)
    args['$nodesFile$']     = simOutput.fileNodesPlotOTGS(configName)

    writeDefaultPythonLauncher(simOutput.pythonLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesPlotOTGS(configName))
        
    args = {}
    args['$EPSILON$']     = str(config.EPSILON)
    args['$singleOrMulti$'] = str(1)

    f = open(simOutput.fileProcessesPlotOTGS(configName), 'w')
    f.write('CONFIG_FILE' + '\t' +
            'PRINT_IO'    + '\n' )

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

            for p1 in xrange(len(simOutput.procList)):
                for p0 in xrange(p1):

                    outputDirList = []
                    labelList     = []
                    for cName in config.OTGS_configurationNames:
                        outputDirList.append(simOutput.performOTGSP0P1FieldSpeciesDir(cName, p0, p1, AOG, field, LOL, species))
                        labelList.append(cName)

                    figDir = simOutput.plotOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species)

                    createDirectories([figDir], config.printIO)
                    args['$figDir$'] = figDir 

                    writeDefaultPlottingConfigOTGSAllConfig(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species), 
                                                            args, outputDirList, labelList, config.OTGS_plottingParametersFileAllConfig)

                    f.write(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species)+'\t')
                    f.write(str(config.printIO)+'\n')

    f.close()

    print('Written '+simOutput.pythonLauncherPlotOTGS(configName)+' ...')
    print('Written '+simOutput.bashLauncherPlotOTGS(configName)+' ...')
    print('Written '+simOutput.fileProcessesPlotOTGS(configName)+' ...')
    print('Written '+simOutput.fileNodesPlotOTGS(configName)+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
