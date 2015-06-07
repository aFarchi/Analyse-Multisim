#!/usr/bin/env python

#_________________
# makeLaunchers.py
#_________________

from analyse.utils.sys.argv                                 import extractArgv
from analyse.preprocess.makeLauncherPreprocess              import makeLauncherPreprocessRawDataForAllSpecies
from analyse.plotting.simulation.makeLauncherPlotSimulation import makeLauncherPlotSimulation
from analyse.plotting.fields.makeLauncherPlotFields         import makeLauncherPlotFields

from analyse.optimalTransport.OTGS.makeLaunchersOTGS        import makeLauncherInterpolateIntoOTGSResolution
from analyse.optimalTransport.OTGS.makeLaunchersOTGS        import makeLauncherMergeOTGSResults
from analyse.optimalTransport.OTGS.makeLaunchersOTGS        import makeLauncherPerformOTGS
from analyse.optimalTransport.OTGS.makeLaunchersOTGS        import makeLauncherPlotOTGSSingleConfig
from analyse.optimalTransport.OTGS.makeLaunchersOTGS        import makeLauncherPlotOTGSMultiConfig

from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherInterpolateIntoOT2DResolution
from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherPerformOT2D
from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherPlotOT2DSingleConfig
from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherPlotOT2DMultiConfig

#__________________________________________________

arguments = extractArgv()

#__________________________________________________

if arguments['FUNCTION'] == 'preprocessRawData':
    makeLauncherPreprocessRawDataForAllSpecies(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotSimulation':
    makeLauncherPlotSimulation(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotFields':
    makeLauncherPlotFields(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'interpolateIntoOTGS':
    makeLauncherInterpolateIntoOTGSResolution(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'mergeOTGSResults':
    makeLauncherMergeOTGSResults(arguments['CONFIG_FILE'])

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
