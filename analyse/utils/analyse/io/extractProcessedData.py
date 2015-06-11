#________________________
# extractProcessedData.py
#________________________

import numpy as np

from navigate            import *
from ..scaling.scaling   import arrayToScaling
from ..scaling.buildTmap import buildTmap

#__________________________________________________

def extractProcessedData(simOutput, procList, AOG, field, LOL, species, TS, applyGlobalScaling, printIO=False):

    datas = {}
    minis = []
    maxis = []

    for proc in procList:
        fn = simOutput.fileProcPreprocessedField(proc, AOG, field, LOL, species, TS)
        if printIO:
            print('Reading '+fn+' ...')
        data        = np.load(fn)
        datas[proc] = data
        minis.append(data.min())
        maxis.append(data.max())

    fn      = simOutput.fileScalingFieldSpecies(AOG, field, LOL, species)
    if printIO:
        print ('Reading '+fn+' ...')
    array   = np.load(fn)
    scaling = arrayToScaling(array)

    if applyGlobalScaling:
        maxi = scaling.maxi
        mini = scaling.mini
    else:
        maxi = np.max(maxis)
        mini = np.min(minis)
        if mini < scaling.mini:
            mini = scaling.mini

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

def extractProcessedDataFullScaling(simOutput, AOG, field, LOL, species, TS, printIO=False):

    datas = {}

    for proc in simOutput.procList:
        fn = simOutput.fileProcPreprocessedField(proc, AOG, field, LOL, species, TS)
        if printIO:
            print('Reading '+fn+' ...')
        data        = np.load(fn)
        datas[proc] = data

    fn = simOutput.fileScalingFieldSpecies(AOG, field, LOL, species)
    if printIO:
        print ('Reading '+fn+' ...')
    array   = np.load(fn)
    scaling = arrayToScaling(array)

    fn = simOutput.fileFMScalingFieldSpecies(AOG, field, LOL, species)
    scalingFM = np.load(fn)

    return (datas, scaling, scalingFM)

#__________________________________________________

def extractProcessedDataForwardTransport(simOutput, configName, p0, p1, AOG, field, LOL, species, TS, printIO=False):

    proc0 = simOutput.procList[p0]
    proc1 = simOutput.procList[p1]
    
    fn = simOutput.applyOTGSForwardP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)
    if printIO:
        print('Reading '+fn+' ...')
    data0 = np.load(fn)

    fn = simOutput.fileProcPreprocessedField(proc1, AOG, field, LOL, species, TS)
    if printIO:
        print('Reading '+fn+' ...')
    data1 = np.load(fn)

    scaling = extractScalingFieldSpecies(simOutput, AOG, field, LOL, species, printIO)

    return (data0, data1, scaling.mini, scaling.maxi)

#__________________________________________________

def extractScalingFieldSpecies(simOutput, AOG, field, LOL, species, printIO=False):
    fn = simOutput.fileScalingFieldSpecies(AOG, field, LOL, species)
    if printIO:
        print ('Reading '+fn+' ...')
    array   = np.load(fn)
    scaling = arrayToScaling(array)

    return scaling

#__________________________________________________

def extractProcessedDataBackwardTransport(simOutput, configName, p0, p1, AOG, field, LOL, species, TS, printIO=False):

    proc0 = simOutput.procList[p0]
    proc1 = simOutput.procList[p1]
    
    fn = simOutput.applyOTGSBackwardP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)
    if printIO:
        print('Reading '+fn+' ...')
    data1 = np.load(fn)

    fn = simOutput.fileProcPreprocessedField(proc0, AOG, field, LOL, species, TS)
    if printIO:
        print('Reading '+fn+' ...')
    data0 = np.load(fn)

    scaling = extractScalingFieldSpecies(simOutput, AOG, field, LOL, species, printIO)

    return (data0, data1, scaling.mini, scaling.maxi)

#__________________________________________________

def extractTmapOTGSP0P1FieldSpecies(simOutput, configName, p0, p1, AOG, field, LOL, species, TS, TmapError, printIO=False):

    fn     = simOutput.TmapFileOTGSP0P1FieldSpecies(configName, p0, p1, AOG, field, LOL, species, TS)
    if printIO:
        print('Reading '+fn+' ...')
    f      = open(fn)
    Tarray = np.load(f)
    Tarray = np.load(f)
    return buildTmap(Tarray, TmapError)

#__________________________________________________
