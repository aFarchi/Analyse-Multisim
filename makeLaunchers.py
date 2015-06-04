#!/usr/bin/env python

#_________________
# makeLaunchers.py
#_________________

from analyse.utils.sys.argv                                 import extractArgv
from analyse.preprocess.makeLauncherPreprocess              import makeLauncherPreprocessRawDataForAllSpecies
from analyse.plotting.simulation.makeLauncherPlotSimulation import makeLauncherPlotSimulation
from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherInterpolateIntoOTResolution
from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherPerformOT2D
from analyse.optimalTransport.OT2D.makeLaunchersOT2D        import makeLauncherPlotOT2D

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

if arguments['FUNCTION'] == 'plotOT2D':
    makeLauncherPlotOT2D(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'interpolateIntoOTResolution':
    makeLauncherInterpolateIntoOTResolution(arguments['CONFIG_FILE'])

#__________________________________________________
