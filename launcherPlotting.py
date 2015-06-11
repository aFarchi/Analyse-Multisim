#!/usr/bin/env python

#____________________
# launcherPlotting.py
#____________________

from analyse.utils.sys.argv                                       import extractArgv
from analyse.plotting.simulation.plotSimulationConfiguration      import PlotSimulationConfiguration
from analyse.plotting.fields.plotFieldsConfiguration              import PlotFieldsConfiguration
from analyse.plotting.applyGSTransport.plotTransportConfiguration import PlotTransportConfiguration

#__________________________________________________

arguments  = extractArgv()
function   = arguments['FUNCTION']
configFile = arguments['CONFIG_FILE']

#__________________________________________________

if function == 'plotSimulation':

    config  = PlotSimulationConfiguration(configFile)
    plotter = config.plotter()

    args    = {}
    try:
        args['AOG']       = arguments['AOG']
        args['GOR']       = arguments['GOR']
        args['species']   = arguments['SPECIES']
        if arguments['PARLLELIZE'] == 'more':
            args['field'] = arguments['FIELD']
            args['LOL']   = arguments['LOL']
    except:
        pass
        
    plotter.plot(**args)

#__________________________________________________

if function == 'plotFields':

    config  = PlotFieldsConfiguration(configFile)
    plotter = config.plotter()

    args    = {}
    try:
        args['AOG']       = arguments['AOG']
        args['species']   = arguments['SPECIES']
        if arguments['PARLLELIZE'] == 'more':
            args['field'] = arguments['FIELD']
            args['LOL']   = arguments['LOL']
    except:
        pass
    plotter.plot(**args)

#__________________________________________________

if function == 'plotApplyGSTransport':

    config  = PlotTransportConfiguration(configFile)
    plotter = config.plotter()

    args              = {}
    try:
        args['AOG']       = arguments['AOG']
        args['species']   = arguments['SPECIES']

        if arguments['PARLLELIZE'] == 'more':
            args['field']      = arguments['FIELD']
            args['LOL']        = arguments['LOL']
            args['TS']         = arguments['TS']
            args['configName'] = arguments['CONFIG_NAME']
    except:
        pass
    plotter.plot(**args)

#__________________________________________________
