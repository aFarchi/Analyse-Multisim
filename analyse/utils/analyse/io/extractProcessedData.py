#________________________
# extractProcessedData.py
#________________________

import numpy as np

from navigate          import *
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

def extractGrayScales(simOutput, procList, AOG, field, LOL, species, scaleGS, printIO=False):

    datas = {}
    minis = []
    maxis = []

    for proc in procList:
        datas[proc] = {}

        for TS in ThresholdNoThreshold():
            fn = simOutput.fileProcPreprocessedFieldGS(proc, AOG, field, LOL, species, TS)
            if printIO:
                print('Reading '+fn+' ...')
            data            = np.load(fn)
            datas[proc][TS] = data

            if TS == 'Threshold':
                minis.append(data.min())
                maxis.append(data.max())

    mini = np.min(minis)
    maxi = np.max(maxis)
    if scaleGS:
        maxi = 1.0

    return (datas, mini, maxi)

#__________________________________________________
