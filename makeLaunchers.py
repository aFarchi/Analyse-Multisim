#!/usr/bin/env python

#_________________
# makeLaunchers.py
#_________________

from analyse.utils.sys.argv                                             import extractArgv

from analyse.preprocess.makeLauncherPreprocess                          import makeLauncherPreprocessRawData

from analyse.plotting.simulation.makeLauncherPlotSimulation             import makeLauncherPlotSimulation
from analyse.plotting.fields.makeLauncherPlotFields                     import makeLauncherPlotFields
from analyse.plotting.applyGSTransport.makeLauncherPlotApplyGSTransport import makeLauncherPlotApplyGSTransport
from analyse.plotting.operators.makeLauncherPlotOperators               import makeLauncherPlotOperators

from analyse.statiticalAnalyse.makeLauncherStatisticalAnalyse           import makeLauncherStatisticalAnalyse

from analyse.optimalTransport.OTGS.makeLaunchersOTGS                    import makeLauncherInterpolateIntoOTGSResolution
from analyse.optimalTransport.OTGS.makeLaunchersOTGS                    import makeLauncherMergeOTGSResults
from analyse.optimalTransport.OTGS.makeLaunchersOTGS                    import makeLauncherPerformOTGS
from analyse.optimalTransport.OTGS.makeLaunchersOTGS                    import makeLauncherPlotOTGSSingleConfig
from analyse.optimalTransport.OTGS.makeLaunchersOTGS                    import makeLauncherPlotOTGSMultiConfig
from analyse.optimalTransport.OTGS.makeLaunchersOTGS                    import makeLauncherApplyGSTransport

from analyse.optimalTransport.OT2D.makeLaunchersOT2D                    import makeLauncherInterpolateIntoOT2DResolution
from analyse.optimalTransport.OT2D.makeLaunchersOT2D                    import makeLauncherMergeOT2DResults
from analyse.optimalTransport.OT2D.makeLaunchersOT2D                    import makeLauncherPerformOT2D
from analyse.optimalTransport.OT2D.makeLaunchersOT2D                    import makeLauncherPlotOT2DSingleConfig
from analyse.optimalTransport.OT2D.makeLaunchersOT2D                    import makeLauncherPlotOT2DMultiConfig

#__________________________________________________

arguments     = extractArgv()
function      = arguments['FUNCTION']
configFile    = arguments['CONFIG_FILE']
availableProc = None
if arguments.has_key('PROCESSORS'):
    availableProc = arguments['PROCESSORS']

#__________________________________________________

if function == 'preprocessRawData':
    makeLauncherPreprocessRawData(configFile, availableProc)

#__________________________________________________

if function == 'plotSimulation':
    makeLauncherPlotSimulation(configFile, availableProc)

#__________________________________________________

if function == 'plotFields':
    makeLauncherPlotFields(configFile, availableProc)

#__________________________________________________

if function == 'plotOperators':
    makeLauncherPlotOperators(configFile, availableProc)

#__________________________________________________

if function == 'plotApplyGSTransport':
    makeLauncherPlotApplyGSTransport(configFile, availableProc)

#__________________________________________________

if function == 'performStatisticalAnalyse':
    makeLauncherStatisticalAnalyse(configFile, availableProc)

#__________________________________________________

if function == 'interpolateIntoOTGSResolution':
    makeLauncherInterpolateIntoOTGSResolution(configFile, availableProc)

#__________________________________________________

if function == 'mergeOTGSResults':
    makeLauncherMergeOTGSResults(configFile, availableProc)

#__________________________________________________

if function == 'applyGSTransport':
    makeLauncherApplyGSTransport(configFile, availableProc)

#__________________________________________________

if function == 'performOTGS':
    makeLauncherPerformOTGS(configFile, availableProc)

#__________________________________________________

if function == 'plotOTGSSingleConfig':
    makeLauncherPlotOTGSSingleConfig(configFile, availableProc)

#__________________________________________________

if function == 'plotOTGSMultiConfig':
    makeLauncherPlotOTGSMultiConfig(configFile, availableProc)

#__________________________________________________

if function == 'performOT2D':
    makeLauncherPerformOT2D(configFile, availableProc)

#__________________________________________________

if function == 'plotOT2DSingleConfig':
    makeLauncherPlotOT2DSingleConfig(configFile, availableProc)

#__________________________________________________

if function == 'plotOT2DMultiConfig':
    makeLauncherPlotOT2DMultiConfig(configFile, availableProc)

#__________________________________________________

if function == 'interpolateIntoOT2DResolution':
    makeLauncherInterpolateIntoOT2DResolution(configFile, availableProc)

#__________________________________________________

if function == 'mergeOT2DResults':
    makeLauncherMergeOT2DResults(configFile, availableProc)

#__________________________________________________
