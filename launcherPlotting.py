#____________________
# launcherPlotting.py
#____________________

from analyse.utils.sys.argv                                  import extractArgv
from analyse.plotting.simulation.plotSimulationConfiguration import PlotSimulationConfiguration

#__________________________________________________

arguments = extractArgv()

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
