#!/usr/bin/env python

#____________
# launcher.py
#____________

from analyse.utils.sys.argv                                    import extractArgv
from analyse.statiticalAnalyse.statisticalAnalyseConfiguration import StatisticalAnalyseConfiguration
from analyse.preprocess.preprocessConfiguration                import PreprocessConfiguration
from analyse.optimalTransport.OTGS.OTGSConfiguration           import OTGSConfiguration 
from analyse.optimalTransport.OT2D.OT2DConfiguration           import OT2DConfiguration 

#__________________________________________________

arguments  = extractArgv()
function   = arguments['FUNCTION']
configFile = arguments['CONFIG_FILE']

#__________________________________________________

if function == 'preprocessRawData':

    config  = PreprocessConfiguration(configFile)
    process = config.process()
    args    = {}

    try:
        args['AOG']     = arguments['AOG']
        args['GOR']     = arguments['GOR']
        args['species'] = arguments['SPECIES']
    except:
        pass

    process.run(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'interpolateIntoOTGSResolution':

    config       = OTGSConfiguration(arguments['CONFIG_FILE'])
    interpolator = config.interpolatorIntoOTGSResolution()
    args         = {}

    try:
        args['AOG']     = arguments['AOG']
        args['GOR']     = arguments['GOR']
        args['species'] = arguments['SPECIES']

        if arguments['PARLLELIZE'] == 'more':
            args['field'] = arguments['FIELD']
            args['LOL']   = arguments['LOL']
            args['TS']    = arguments['TS']
    except:
        pass

    interpolator.run(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'mergeOTGSResults':

    config       = OTGSConfiguration(arguments['CONFIG_FILE'])
    merger       = config.OTGSResultMerger()
    args         = {}

    try:
        args['AOG']     = arguments['AOG']
        args['GOR']     = arguments['GOR']
        args['species'] = arguments['SPECIES']

        if arguments['PARLLELIZE'] == 'more':
            args['field']      = arguments['FIELD']
            args['LOL']        = arguments['LOL']
            args['TS']         = arguments['TS']
            args['configName'] = arguments['CONFIG_NAME']
    except:
        pass

    merger.run(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'applyGSTransport':

    config       = OTGSConfiguration(arguments['CONFIG_FILE'])
    applier      = config.OTGSTransportApplier()
    args         = {}

    try:
        args['AOG']     = arguments['AOG']
        args['species'] = arguments['SPECIES']

        if arguments['PARLLELIZE'] == 'more':
            args['field']      = arguments['FIELD']
            args['LOL']        = arguments['LOL']
            args['TS']         = arguments['TS']
            args['configName'] = arguments['CONFIG_NAME']
    except:
        pass

    applier.run(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'interpolateIntoOT2DResolution':

    config       = OT2DConfiguration(arguments['CONFIG_FILE'])
    interpolator = config.interpolatorIntoOT2DResolution()
    args         = {}

    try:
        args['AOG']     = arguments['AOG']
        args['GOR']     = arguments['GOR']
        args['species'] = arguments['SPECIES']

        if arguments['PARLLELIZE'] == 'more':
            args['field'] = arguments['FIELD']
            args['LOL']   = arguments['LOL']
    except:
        pass

    interpolator.run(**args)

#__________________________________________________

if arguments['FUNCTION'] == 'mergeOT2DResults':

    config       = OT2DConfiguration(arguments['CONFIG_FILE'])
    merger       = config.OT2DResultMerger()
    args         = {}

    try:
        args['AOG']     = arguments['AOG']
        args['GOR']     = arguments['GOR']
        args['species'] = arguments['SPECIES']

        if arguments['PARLLELIZE'] == 'more':
            args['field']      = arguments['FIELD']
            args['LOL']        = arguments['LOL']
            args['configName'] = arguments['CONFIG_NAME']
    except:
        pass

    merger.run(**args)

#__________________________________________________

if function == 'performStatisticalAnalyse':

    config   = StatisticalAnalyseConfiguration(configFile)
    analyser = config.analyser()
    args     = {}

    try:
        args['AOG']     = arguments['AOG']
        args['species'] = arguments['SPECIES']

        if arguments['PARLLELIZE'] == 'more':
            args['field']      = arguments['FIELD']
            args['LOL']        = arguments['LOL']
    except:
        pass

    analyser.run(**args)

#__________________________________________________
