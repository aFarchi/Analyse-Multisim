#!/usr/bin/env python

#_________________
# makeLaunchers.py
#_________________

from analyse.utils.sys.argv                                             import extractArgv

from analyse.preprocess.makeLauncherPreprocess                          import makeLauncherPreprocessRawData

from analyse.plotting.simulation.makeLauncherPlotSimulation             import makeLauncherPlotSimulation
from analyse.plotting.fields.makeLauncherPlotFields                     import makeLauncherPlotFields
from analyse.plotting.applyGSTransport.makeLauncherPlotApplyGSTransport import makeLauncherPlotApplyGSTransport

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

if arguments['FUNCTION'] == 'plotSimulation':
    makeLauncherPlotSimulation(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotFields':
    makeLauncherPlotFields(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotApplyGSTransport':
    makeLauncherPlotApplyGSTransport(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'performStatisticalAnalyse':
    makeLauncherStatisticalAnalyse(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'interpolateIntoOTGSResolution':
    makeLauncherInterpolateIntoOTGSResolution(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'mergeOTGSResults':
    makeLauncherMergeOTGSResults(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'applyGSTransport':
    makeLauncherApplyGSTransport(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'performOTGS':
    makeLauncherPerformOTGS(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotOTGSSingleConfig':
    makeLauncherPlotOTGSSingleConfig(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotOTGSMultiConfig':
    makeLauncherPlotOTGSMultiConfig(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'performOT2D':
    makeLauncherPerformOT2D(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotOT2DSingleConfig':
    makeLauncherPlotOT2DSingleConfig(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotOT2DMultiConfig':
    makeLauncherPlotOT2DMultiConfig(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'interpolateIntoOT2DResolution':
    makeLauncherInterpolateIntoOT2DResolution(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'mergeOT2DResults':
    makeLauncherMergeOT2DResults(arguments['CONFIG_FILE'])

#__________________________________________________
