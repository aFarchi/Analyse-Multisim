#__________________
# extractRawData.py
#__________________

import numpy as np

from ..io.navigate import *

#__________________________________________________

def extractRawData(simOutput, proc, AOG, GOR, species, printIO=False):

    speciesBinList = simOutput.simConfig.speciesBinList[GOR][species]
    rawShape       = simOutput.simConfig.rawShapes[GOR][AOG]
    deltaT         = simOutput.simConfig.deltaT

    rawSize        = 1
    for dim in xrange(len(rawShape)):
        rawSize   *= rawShape[dim]

    rawData        = np.zeros(rawSize)

    for speciesBin in speciesBinList:
        for DOW in DryOrWet(AOG):
            for IOB in InCloudOrBelowCould(AOG, GOR)[DOW]:
                fileName = simOutput.fileSpeciesBinProc(proc, DOW, IOB, speciesBin)
                if printIO:
                    print ('Reading '+fileName+' ...')
                try:
                    rawData += np.fromfile(fileName, 'f') 
                except:
                    print('Could not read file : '+fileName)

    rawData = rawData.reshape(rawShape)
    if 'air' in AOG:
        return rawData
    elif 'ground' in AOG:
        return rawData[:,0,:,:].cumsum(axis=0)*deltaT

#__________________________________________________

def extractRawDataMultiProc(simOutput, AOG, GOR, species, printIO):
    rawData = {}
    for proc in simOutput.procList:
        rawData[proc] = extractRawData(simOutput, proc, AOG, GOR, species, printIO)

    return rawData

#__________________________________________________

def extractFieldAllIterations(rawData, simOutput, field, lol):
    data  = {}
    minis = []
    maxis = []
    for proc in simOutput.procList:
        data[proc] = field.extractAllIterations(rawData[proc], lol)
        minis.append(data[proc].min())
        maxis.append(data[proc].max())
        tmax       = data[proc].shape[0]
        
    mini  = np.min(minis)
    maxi  = np.min(maxis)

    return (data, mini, maxi, tmax)

#__________________________________________________
