#!/usr/bin/env python

#____________
# launcher.py
#____________

from analyse.utils.sys.argv                          import extractArgv
from analyse.preprocess.preprocessConfiguration      import PreprocessConfiguration
from analyse.optimalTransport.OT2D.OT2DConfiguration import OT2DConfiguration 

#__________________________________________________

arguments = extractArgv()

#__________________________________________________

if arguments['FUNCTION'] == 'preprocessRawData':

    config  = PreprocessConfiguration(arguments['CONFIG_FILE'])
    process = config.process()
    args    = {}

    if arguments['RUN_AOO'] == 'one':
        args['AOG']     = arguments['AOG']
        args['GOR']     = arguments['GOR']
        args['species'] = arguments['SPECIES']

    process.run(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'interpolateIntoOT2DResolutionDir':

    config       = OT2DConfiguration(arguments['CONFIG_FILE'])
    interpolator = config.interpolatorIntoOT2DResolution()
    args         = {}

    if arguments['RUN_AOO'] == 'one':
        args['AOG']     = arguments['AOG']
        args['GOR']     = arguments['GOR']
        args['species'] = arguments['SPECIES']

    interpolator.run(**args)

#__________________________________________________
