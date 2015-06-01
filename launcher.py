#!/usr/bin/env python

#____________
# launcher.py
#____________

from analyse.utils.sys.argv                     import extractArgv
from analyse.preprocess.preprocessConfiguration import PreprocessConfiguration

#__________________________________________________

arguments = extractArgv()

#__________________________________________________

if arguments['FUNCTION'] == 'preprocessRawData':

    config  = PreprocessConfiguration(arguments['CONFIG_FILE'])
    process = config.process()
    args    = {}

    if arguments['RUN_AOO'] == 'one':
        args['AOG']       = arguments['AOG']
        args['GOR']       = arguments['GOR']
        args['species']   = arguments['SPECIES']

    process.run(**args)

#__________________________________________________
