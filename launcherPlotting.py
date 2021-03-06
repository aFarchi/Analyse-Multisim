#!/usr/bin/env python

#____________________
# launcherPlotting.py
#____________________

from analyse.utils.sys.argv                                       import extractArgv
from analyse.plotting.simulation.plotSimulationConfiguration      import PlotSimulationConfiguration
from analyse.plotting.fields.plotFieldsConfiguration              import PlotFieldsConfiguration
from analyse.plotting.applyGSTransport.plotTransportConfiguration import PlotTransportConfiguration

#__________________________________________________

arguments = extractArgv()

#__________________________________________________

if arguments['FUNCTION'] == 'plotSimulation':

    config  = PlotSimulationConfiguration(arguments['CONFIG_FILE'])
    plotter = config.plotter()

    args              = {}
    args['AOG']       = arguments['AOG']
    args['GOR']       = arguments['GOR']
    args['species']   = arguments['SPECIES']

    if arguments['PARLLELIZE'] == 'more':
        args['field'] = arguments['FIELD']
        args['LOL']   = arguments['LOL']
        
    plotter.plot(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'plotFields':

    config  = PlotFieldsConfiguration(arguments['CONFIG_FILE'])
    plotter = config.plotter()

    args              = {}
    args['AOG']       = arguments['AOG']
    args['GOR']       = arguments['GOR']
    args['species']   = arguments['SPECIES']

    if arguments['PARLLELIZE'] == 'more':
        args['field'] = arguments['FIELD']
        args['LOL']   = arguments['LOL']
        
    plotter.plot(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'plotApplyGSTransport':

    config  = PlotTransportConfiguration(arguments['CONFIG_FILE'])
    plotter = config.plotter()

    args              = {}
    args['AOG']       = arguments['AOG']
    args['species']   = arguments['SPECIES']

    if arguments['PARLLELIZE'] == 'more':
        args['field']      = arguments['FIELD']
        args['LOL']        = arguments['LOL']
        args['TS']         = arguments['TS']
        args['configName'] = arguments['CONFIG_NAME']
        
    plotter.plot(**args)

#__________________________________________________
