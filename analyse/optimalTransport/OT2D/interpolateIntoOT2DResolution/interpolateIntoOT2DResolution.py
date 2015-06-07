#_________________________________
# interpolateIntoOT2DResolution.py
#_________________________________

import numpy as np

from itertools                     import product

#__________________________________________________

def interpolateAOGFieldsIntoOT2DResolution(simOutput,
                                           AOG,
                                           species,
                                           field,
                                           LOL,
                                           proc,
                                           OTShape,
                                           printIO):

    fn   = simOutput.fileProcPreprocessedField(proc, AOG, field, LOL, species)
    if printIO:
        print ('Reading '+fn+' ...')
    data = np.load(fn)
    data = field.interpolate(data, OTShape)

    fn = simOutput.fileProcPreprocessedFieldOTResolution(proc, AOG, field, LOL, species)
    if printIO:
        print ('Writing '+fn+' ...')
    np.save(fn, data)

#__________________________________________________
