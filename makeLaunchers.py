#!/usr/bin/env python

#_________________
# makeLaunchers.py
#_________________

from analyse.utils.sys.argv                                 import extractArgv
from analyse.preprocess.makeLauncherPreprocess              import makeLauncherPreprocessRawDataForAllSpecies
from analyse.plotting.simulation.makeLauncherPlotSimulation import makeLauncherPlotSimulation

#__________________________________________________

arguments = extractArgv()

#__________________________________________________

if arguments['FUNCTION'] == 'preprocessRawData':
    makeLauncherPreprocessRawDataForAllSpecies(arguments['CONFIG_FILE'])

#__________________________________________________

if arguments['FUNCTION'] == 'plotSimulation':
    makeLauncherPreprocessRawDataForAllSpecies(arguments['CONFIG_FILE'])

#__________________________________________________
