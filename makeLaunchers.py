#!/usr/bin/env python

#_________________
# makeLaunchers.py
#_________________

from analyse.utils.sys.argv                                 import extractArgv
from analyse.preprocess.makeLauncherPreprocess              import makeLauncherPreprocessRawDataForAllSpecies
from analyse.plotting.simulation.makeLauncherPlotSimulation import makeLauncherPlotSimulation
from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherInterpolateIntoOTResolution
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
    makeLauncherPreprocessRawDataForAllSpecies(arguments['CONFIG_FILE'])

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

if arguments['FUNCTION'] == 'interpolateIntoOTResolution':
    makeLauncherInterpolateIntoOTResolution(arguments['CONFIG_FILE'])

#__________________________________________________
