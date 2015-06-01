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
from ...utils.io.writeOTConfig                            import writeDefaultPlottingConfigOT2D
from ...utils.analyse.timeSelection.defaultTimeResolution import minTimeRes
from ...utils.analyse.timeSelection.defaultTimeResolution import maxTimeRes

#__________________________________________________

def makeLauncherPerformOT2D(configFile):

    config    = OT2DConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    if config.OT2D_timeResFunction == 'min':
        timeResFunction = minTimeRes
    elif config.OT2D_timeResFunction == 'max':
        timeResFunction = maxTimeRes

    for algoName in config.OT2D_algoNames:

        createDirectories([simOutput.launcherPerformOT2DDir(algoName)], config.printIO)

        args                    = {}
        args['$fileProcesses$'] = simOutput.fileProcessesPerformOT2D(algoName)
        args['$launcher$']      = simOutput.modulePath.OT2DLauncher
        args['$interpretor$']   = 'python'
        args['$startString$']   = 'Starting OT2D ...'
        
        args['$logFile$']       = simOutput.fileLogPerformOT2D(algoName)
        args['$nodesFile$']     = simOutput.fileNodesPerformOT2D(algoName)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPerformOT2D(algoName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPerformOT2D(algoName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPerformOT2D(algoName))
        
        args = {}
        args['$EPSILON$']    = str(config.EPSILON)
        args['$dynamics$']   = config.OT2D_dynamics[algoName]
        args['$normType$']   = config.OT2D_normType[algoName]
        args['$algoName$']   = algoName
        args['$iterTarget$'] = config.OT2D_iterTarget[algoName]
        args['$nModPrint$']  = config.OT2D_nModPrint[algoName]
        args['$nModWrite$']  = config.OT2D_nModWrite[algoName]
        args['$gamma$']      = config.OT2D_gamma
        args['$alpha$']      = config.OT2D_alpha
        args['$theta$']      = config.OT2D_theta
        args['$sigma$']      = config.OT2D_sigma
        args['$tau$']        = config.OT2D_tau
        args['$gamma3$']     = config.OT2D_gamma3
        args['$alpha3$']     = config.OT2D_alpha3
        args['$omega1$']     = config.OT2D_omega1
        args['$omega2$']     = config.OT2D_omega2
        args['$omega3$']     = config.OT2D_omega3
        args['$initial$']    = config.OT2D_initial[algoName]
        args['$initialID$']  = config.OT2D_initialID[algoName]

        f = open(simOutput.fileProcessesPerformOT2D(algoName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        directory = simOutput.performOT2DP0P1FieldSpeciesDir(algoName, p0, p1, AOG, field, LOL, species)
                        createDirectories([directory], config.printIO)

                        M = config.preprocessRawData_analyseShape[field.axes[0]]
                        N = config.preprocessRawData_analyseShape[field.axes[1]]

                        args['$outputDir$'] = directory
                        args['$M$']         = str(M)
                        args['$N$']         = str(N)
                        args['$P$']         = str(timeResFunction(M, N))

                        args['$filef0$']    = simOutput.fileProcPreprocessedField(simOutput.procList[p0], AOG, field, LOL, species)
                        args['$filef1$']    = simOutput.fileProcPreprocessedField(simOutput.procList[p1], AOG, field, LOL, species)

                        writeDefaultConfigOT2D(simOutput.configFilePerformOT2DP0P1FieldSpecies(algoName, p0, p1, AOG, field, LOL, species), args)

                        f.write(simOutput.configFilePerformOT2DP0P1FieldSpecies(algoName, p0, p1, AOG, field, LOL, species)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPerformOT2D(algoName)+' ...')
        print('Written '+simOutput.bashLauncherPerformOT2D(algoName)+' ...')
        print('Written '+simOutput.fileProcessesPerformOT2D(algoName)+' ...')
        print('Written '+simOutput.fileNodesPerformOT2D(algoName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________

def makeLauncherPlotOT2D(configFile):

    config    = OT2DConfiguration(configFile)
    simOutput = buildSimulationsOutput(config)

    for algoName in config.OT2D_algoNames:

        createDirectories([simOutput.launcherPlotOT2DDir(algoName)], config.printIO)

        args                    = {}
        args['$fileProcesses$'] = simOutput.fileProcessesPlotOT2D(algoName)
        args['$launcher$']      = simOutput.modulePath.OT2DLauncherPlotting
        args['$interpretor$']   = 'python'
        args['$startString$']   = 'Plotting OT2D ...'
        
        args['$logFile$']       = simOutput.fileLogPlotOT2D(algoName)
        args['$nodesFile$']     = simOutput.fileNodesPlotOT2D(algoName)

        writeDefaultPythonLauncher(simOutput.pythonLauncherPlotOT2D(algoName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultBashLauncher(simOutput.bashLauncherPlotOT2D(algoName), args, makeExecutable=True, printIO=config.printIO)
        writeDefaultNodesFile(simOutput.fileNodesPlotOT2D(algoName))
        
        args = {}
        args['$EPSILON$']    = str(config.EPSILON)

        f = open(simOutput.fileProcessesPlotOT2D(algoName), 'w')
        f.write('CONFIG_FILE' + '\t' +
                'PRINT_IO'    + '\n' )

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for (species, field, LOL) in product(simOutput.simConfig.speciesList[GOR], simOutput.fieldList[AOG], LinOrLog()):

                for p1 in xrange(len(simOutput.procList)):
                    for p0 in xrange(p1):

                        outputDir = simOutput.performOT2DP0P1FieldSpeciesDir(algoName, p0, p1, AOG, field, LOL, species)
                        figDir    = simOutput.plotOT2DP0P1FieldSpeciesDir(algoName, p0, p1, AOG, field, LOL, species)
                        label     = str(p0) + '-' + str(p1) + ', ' + algoName

                        createDirectories([figDir], config.printIO)
                        args['$figDir$']    = figDir 
                        args['$outputDir$'] = outputDir
                        args['$label$']     = label

                        writeDefaultPlottingConfigOT2D(simOutput.configFilePlotOT2DP0P1FieldSpecies(algoName, p0, p1, AOG, field, LOL, species), 
                                                       args, config.OT2D_plottingParametersFile)

                        f.write(simOutput.configFilePlotOT2DP0P1FieldSpecies(algoName, p0, p1, AOG, field, LOL, species)+'\t')
                        f.write(str(config.printIO)+'\n')

        f.close()

        print('Written '+simOutput.pythonLauncherPlotOT2D(algoName)+' ...')
        print('Written '+simOutput.bashLauncherPlotOT2D(algoName)+' ...')
        print('Written '+simOutput.fileProcessesPlotOT2D(algoName)+' ...')
        print('Written '+simOutput.fileNodesPlotOT2D(algoName)+' ...')

        print('Do not forget to specify nodes / log files and number of processes.')

#__________________________________________________
