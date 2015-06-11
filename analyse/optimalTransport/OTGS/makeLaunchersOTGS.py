#_____________________
# makeLaunchersOTGS.py
#_____________________

from itertools                                            import product

from OTGSConfiguration                                    import OTGSConfiguration
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

def makeLauncherInterpolateIntoOTGSResolution(configFile, availableProc=None):
    
    config    = OTGSConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherInterpolateIntoOTGSResolutionFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherInterpolateIntoOTGSResolutionFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherInterpolateIntoOTGSResolutionFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'
    args['$logFile$']       = simOutput.launcherInterpolateIntoOTGSResolutionFiles['log']
    args['$nodesFile$']     = simOutput.launcherInterpolateIntoOTGSResolutionFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherInterpolateIntoOTGSResolutionFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherInterpolateIntoOTGSResolutionFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherInterpolateIntoOTGSResolutionFiles['nodes'])
    
    f = open(simOutput.launcherInterpolateIntoOTGSResolutionFiles['processes'], 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'PARLLELIZE'  + '\t' +
            'AOG'         + '\t' +
            'SPECIES'     + '\t' +
            'FIELD'       + '\t' +
            'LOL'         + '\t' +
            'TS'          + '\n' )

    dirsToCreate = []
    for (AOG, LOL) in product(AirOrGround(), LinOrLog()):
        for (field, proc) in product(simOutput.fieldList[AOG], simOutput.procList):
            dirsToCreate.append(simOutput.procPreprocessedFieldOTResolutionDir(proc, AOG, field, LOL))

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:

            if config.OTGS_interpolateIntoOTGSResolution_parallelize == 'less':
                f.write('interpolateIntoOTGSResolution'                                + '\t' +
                        simOutput.launcherInterpolateIntoOTGSResolutionFiles['config'] + '\t' +
                        'less'                                                         + '\t' +
                        AOG                                                            + '\t' +
                        species                                                        + '\t' +
                        'None'                                                         + '\t' +
                        'None'                                                         + '\t' +
                        'None'                                                         + '\n' )

            elif config.OTGS_interpolateIntoOTGSResolution_parallelize =='more':                
                for (field, LOL, TS) in product(simOutput.fieldList[AOG], LinOrLog(), ThresholdNoThreshold()):
                    f.write('interpolateIntoOTGSResolution'                                + '\t' +
                            simOutput.launcherInterpolateIntoOTGSResolutionFiles['config'] + '\t' +
                            'more'                                                         + '\t' +
                            AOG                                                            + '\t' +
                            species                                                        + '\t' +
                            field.name                                                     + '\t' +
                            LOL                                                            + '\t' +
                            TS                                                             + '\n' )

    f.close()

    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherInterpolateIntoOTGSResolutionFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherInterpolateIntoOTGSResolutionFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherInterpolateIntoOTGSResolutionFiles['processes']+' ...')
    print('Written '+simOutput.launcherInterpolateIntoOTGSResolutionFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherMergeOTGSResults(configFile, availableProc=None):
    
    config    = OTGSConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherMergeOTGSResultsFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherMergeOTGSResultsFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherMergeOTGSResultsFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Merging OTGS results'
    args['$logFile$']       = simOutput.launcherMergeOTGSResultsFiles['log']
    args['$nodesFile$']     = simOutput.launcherMergeOTGSResultsFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherMergeOTGSResultsFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherMergeOTGSResultsFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherMergeOTGSResultsFiles['nodes'])

    f = open(simOutput.launcherMergeOTGSResultsFiles['processes'], 'w')
    f.write('FUNCTION'    + '\t' +
            'CONFIG_FILE' + '\t' +
            'PARLLELIZE'  + '\t' +
            'AOG'         + '\t' +
            'SPECIES'     + '\t' +
            'FIELD'       + '\t' +
            'LOL'         + '\t' +
            'TS'          + '\t' +
            'CONFIG_NAME' + '\n' )

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:

            if config.OTGS_mergeOTGSResults_parallelize == 'less':
                f.write('mergeOTGSResults'                                + '\t' +
                        simOutput.launcherMergeOTGSResultsFiles['config'] + '\t' +
                        'less'                                            + '\t' +
                        AOG                                               + '\t' +
                        species                                           + '\t' +
                        'None'                                            + '\t' +
                        'None'                                            + '\t' +
                        'None'                                            + '\t' +
                        'None'                                            + '\n' )

            elif config.OTGS_mergeOTGSResults_parallelize =='more':
                
                for (field, LOL, TS, configName) in product(simOutput.fieldList[AOG], LinOrLog(), ThresholdNoThreshold(), config.OTGS_configurationNames):
                    f.write('mergeOTGSResults'                                + '\t' +
                            simOutput.launcherMergeOTGSResultsFiles['config'] + '\t' +
                            'more'                                            + '\t' +
                            AOG                                               + '\t' +
                            species                                           + '\t' +
                            field.name                                        + '\t' +
                            LOL                                               + '\t' +
                            TS                                                + '\t' +
                            configName                                        + '\n' )

    f.close()

    print('Written '+simOutput.launcherMergeOTGSResultsFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherMergeOTGSResultsFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherMergeOTGSResultsFiles['processes']+' ...')
    print('Written '+simOutput.launcherMergeOTGSResultsFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPerformOTGS(configFile, availableProc=None):

    config    = OTGSConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    for configName in config.OTGS_configurationNames:

        createDirectories([simOutput.launcherPerformOTGSDir(configName)], config.printIO)

        args                    = {}
        args['$fileProcesses$'] = simOutput.fileProcessesPerformOTGS(configName)
        args['$launcher$']      = simOutput.modulePath.OT1DLauncher
        args['$interpretor$']   = 'python'
        args['$startString$']   = 'Starting OTGS ...'
        args['$logFile$']       = simOutput.fileLogPerformOTGS(configName)
        args['$nodesFile$']     = simOutput.fileNodesPerformOTGS(configName)
        if availableProc is not None:
            args['$nProcessors$'] = str(availableProc)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPerformOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPerformOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPerformOTGS(configName))
        
        args = {}
        args['$EPSILON$']    = str(config.EPSILON)
    
        f = open(simOutput.fileProcessesPerformOTGS(configName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL, TS) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog(), ThresholdNoThreshold()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        directory = simOutput.performOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS)
                        createDirectories([directory], config.printIO)
                        
                        N = config.OTGS_resolution
                        
                        args['$outputDir$'] = directory
                        args['$N$']         = str(N)
                        args['$P$']         = str(N)

                        args['$filef0$']    = simOutput.fileProcPreprocessedFieldGSOTResolution(simOutput.procList[p0], AOG, field, LOL, species, TS)
                        args['$filef1$']    = simOutput.fileProcPreprocessedFieldGSOTResolution(simOutput.procList[p1], AOG, field, LOL, species, TS)

                        writeDefaultConfigOTGS(simOutput.configFilePerformOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS), 
                                               args, config.OTGS_algorithmParametersFiles[configName])

                        f.write(simOutput.configFilePerformOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPerformOTGS(configName)+' ...')
        print('Written '+simOutput.bashLauncherPerformOTGS(configName)+' ...')
        print('Written '+simOutput.fileProcessesPerformOTGS(configName)+' ...')
        print('Written '+simOutput.fileNodesPerformOTGS(configName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPlotOTGSSingleConfig(configFile, availableProc=None):

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
        if availableProc is not None:
            args['$nProcessors$'] = str(availableProc)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPlotOTGS(configName))
        
        args = {}
        args['$EPSILON$']       = str(config.EPSILON)
        args['$singleOrMulti$'] = 'single'

        f = open(simOutput.fileProcessesPlotOTGS(configName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL, TS) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog(), ThresholdNoThreshold()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        outputDir = simOutput.performOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS)
                        figDir    = simOutput.plotOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS)
                        label     = str(p0) + '-' + str(p1) + ', ' + configName

                        createDirectories([figDir], config.printIO)
                        args['$figDir$']    = figDir 
                        args['$outputDir$'] = outputDir
                        args['$label$']     = label

                        writeDefaultPlottingConfigOTGS(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS), 
                                                       args, config.OTGS_plottingParametersFiles[configName])

                        f.write(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPlotOTGS(configName)+' ...')
        print('Written '+simOutput.bashLauncherPlotOTGS(configName)+' ...')
        print('Written '+simOutput.fileProcessesPlotOTGS(configName)+' ...')
        print('Written '+simOutput.fileNodesPlotOTGS(configName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPlotOTGSMultiConfig(configFile, availableProc=None):

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
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.pythonLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.bashLauncherPlotOTGS(configName), args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.fileNodesPlotOTGS(configName))
        
    args = {}
    args['$EPSILON$']       = str(config.EPSILON)
    args['$singleOrMulti$'] = 'multi'

    f = open(simOutput.fileProcessesPlotOTGS(configName), 'w')
    f.write('CONFIG_FILE' + '\t' +
            'PRINT_IO'    + '\n' )

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for (species, field, LOL, TS) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog(), ThresholdNoThreshold()):

            for p1 in xrange(len(simOutput.procList)):
                for p0 in xrange(p1):

                    outputDirList = []
                    labelList     = []
                    for cName in config.OTGS_configurationNames:
                        outputDirList.append(simOutput.performOTGSP0P1FieldSpeciesDir(cName, p0, p1, AOG, field, LOL, species, TS))
                        labelList.append(cName)

                    figDir = simOutput.plotOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS)

                    createDirectories([figDir], config.printIO)
                    args['$figDir$'] = figDir 

                    writeDefaultPlottingConfigOTGSAllConfig(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS), 
                                                            args, outputDirList, labelList, config.OTGS_plottingParametersFileAllConfig)

                    f.write(simOutput.configFilePlotOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)+'\t')
                    f.write(str(config.printIO)+'\n')

    f.close()

    print('Written '+simOutput.pythonLauncherPlotOTGS(configName)+' ...')
    print('Written '+simOutput.bashLauncherPlotOTGS(configName)+' ...')
    print('Written '+simOutput.fileProcessesPlotOTGS(configName)+' ...')
    print('Written '+simOutput.fileNodesPlotOTGS(configName)+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherApplyGSTransport(configFile, availableProc=None):
    
    config    = OTGSConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    createDirectories([simOutput.launcherApplyGSTransportFiles['directory']], config.printIO)
    config.writeConfig(simOutput.launcherApplyGSTransportFiles['config'])

    args                    = {}
    args['$fileProcesses$'] = simOutput.launcherApplyGSTransportFiles['processes']
    args['$launcher$']      = simOutput.modulePath.moduleLauncher
    args['$interpretor$']   = 'python'
    args['$startString$']   = 'Preparing all fields'
    args['$logFile$']       = simOutput.launcherApplyGSTransportFiles['log']
    args['$nodesFile$']     = simOutput.launcherApplyGSTransportFiles['nodes']
    if availableProc is not None:
        args['$nProcessors$'] = str(availableProc)

    writeDefaultPythonLauncher(simOutput.launcherApplyGSTransportFiles['pyLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultBashLauncher(simOutput.launcherApplyGSTransportFiles['shLauncher'], args, makeExecutable=True, printIO=config.printIO)
    writeDefaultNodesFile(simOutput.launcherApplyGSTransportFiles['nodes'])
    
    f = open(simOutput.launcherApplyGSTransportFiles['processes'], 'w')
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
            for (field, LOL, TS, configName) in product(simOutput.fieldList[AOG], LinOrLog(), ThresholdNoThreshold(), config.OTGS_configurationNames):
                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):
                        dirsToCreate.append(simOutput.applyOTGSP0P1FieldSpeciesDir(configName, p0, p1, AOG, field, LOL, species, TS))

            if config.OTGS_applyOTGS_parallelize == 'less':
                f.write('applyGSTransport'                                + '\t' +
                        simOutput.launcherApplyGSTransportFiles['config'] + '\t' +
                        'less'                                            + '\t' +
                        AOG                                               + '\t' +
                        species                                           + '\t' +
                        'None'                                            + '\t' +
                        'None'                                            + '\t' +
                        'None'                                            + '\t' +
                        'None'                                            + '\n' )

            elif config.OTGS_applyOTGS_parallelize =='more':
                
                for (field, LOL, TS, configName) in product(simOutput.fieldList[AOG], LinOrLog(), ThresholdNoThreshold(), config.OTGS_configurationNames):
                    f.write('applyGSTransport'                                + '\t' +
                            simOutput.launcherApplyGSTransportFiles['config'] + '\t' +
                            'more'                                            + '\t' +
                            AOG                                               + '\t' +
                            species                                           + '\t' +
                            field.name                                        + '\t' +
                            LOL                                               + '\t' +
                            TS                                                + '\t' +
                            configName                                        + '\n' )

    f.close()
    createDirectories(dirsToCreate, config.printIO)
    print('Written '+simOutput.launcherApplyGSTransportFiles['pyLauncher']+' ...')
    print('Written '+simOutput.launcherApplyGSTransportFiles['shLauncher']+' ...')
    print('Written '+simOutput.launcherApplyGSTransportFiles['processes']+' ...')
    print('Written '+simOutput.launcherApplyGSTransportFiles['nodes']+' ...')

    print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
