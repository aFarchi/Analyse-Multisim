#________________________
# extractProcessedData.py
#________________________

import numpy as np

from ..scaling.scaling import arrayToScaling

#__________________________________________________

def extractProcessedData(simOutput, procList, AOG, field, LOL, species, applyGlobalScaling, printIO=False):

    datas = {}
    minis = []
    maxis = []

    for proc in procList:
        fn = simOutput.fileProcPreprocessedField(proc, AOG, field, LOL, species)
        if printIO:
            print('Reading '+fn+' ...')
        data        = np.load(fn)
        datas[proc] = data
        minis.append(data.min())
        maxis.append(data.max())

    if applyGlobalScaling:
        
        fn      = simOutput.fileScalingFieldSpecies(AOG, field, LOL, species)
        if printIO:
            print ('Reading '+fn+' ...')
        array   = np.load(fn)
        scaling = arrayToScaling(array)

        mini    = scaling.mini
        maxi    = scaling.maxi

    else:
        mini    = np.min(minis)
        maxi    = np.max(maxis)

    return (datas, mini, maxi)

#__________________________________________________
