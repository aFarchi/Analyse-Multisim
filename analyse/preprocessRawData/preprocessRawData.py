#_____________________
# preprocessRawData.py
#_____________________

import numpy as np

from itertools                                     import product

from ..utils.analyse.scaling.scaling               import initScalingMaximum
from ..utils.analyse.scaling.scaling               import mergeScalings
from ..utils.analyse.scaling.scaling               import writeScaling
from ..utils.analyse.scaling.fmscaling             import initScalingFM
from ..utils.analyse.scaling.fmscaling             import mergeFMScalings
from ..utils.analyse.scaling.fmscaling             import writeFMScaling
from ..utils.analyse.processRawData.extractRawData import extractRawData
from ..utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ..utils.analyse.io.navigate                   import *

#__________________________________________________

def computeAOGFields(preprocessConfig, simOutput, AOG, GOR, species):
    
    (scaling, maximum) = initScalingMaximum(simOutput)

    for proc in simOutput.procList:

        rawData = extractRawData(simOutput, proc, AOG, GOR, species, preprocessConfig.printIO)

        for (field, lol) in product(simOutput.fieldList, LinOrLog()):

            (data, scale) = field.extract(rawData[proc], lol)
                        
            try:
                maximum[lol][field] = np.maximum( maximum[lol][field] , data )
            except:
                maximum[lol][field] = data

            scaling[lol][field][proc] = scale
            data                      = field.interpolate(data, preprocessConfig.analyseShape)

            fn = simOutput.fileProcPreprocessedField(proc, AOG, field, lol, species)
            if printIO:
                print ('Writing '+fn+' ...')
            np.save(fn, data)

    scaling = mergeScalings(simOutput, scaling, maximum)
    writeScaling(simOutput, scaling, species, AOG, preprocessConfig.printIO)                                

#__________________________________________________

def computeFMScalingMakeGSAOGFields(preprocessConfig, simOutput, AOG, GOR, species):

    scalingFM = initScalingFM(simOutput)

    for proc in simOutput.procList:

        rawData = extractRawData(simOutput, proc, AOG, GOR, species, preprocessConfig.printIO)

        for (field, lol) in product(simOutput.fieldList, LinOrLog()):

            fn      = simOutput.fileScalingFieldSpecies(AOG, field, lol, species)
            array   = np.load(fn)
            scaling = arrayToScaling(array)
            
            (FMScaling, GSNT, GST)      = field.computeFMScalingMakeGS(rawData[proc], lol, scaling.mini, scaling.maxi, preprocessConfig.nLevelsAnalyse)
            scalingFM[lol][field][proc] = FMScaling

            fn = simOutput.fileGSToAnalyse(proc, AOG, field, lol, species, 'Threshold')
            if printIO:
                print ('Writing '+fn+' ...')
            np.save(fn, GST)

            fn = simOutput.fileGSToAnalyse(proc, AOG, field, lol, species, 'NoThreshold')
            if printIO:
                print ('Writing '+fn+' ...')
            np.save(fn, GSNT)

    scalingFM = mergeFMScalings(simOutput, scalingFM)
    writeFMScaling(simOutput, scalingFM, species, AOG, simOutput.printIO)

#__________________________________________________

def preprocessRawDataForSpecies(preprocessConfig, AOG, GOR, species, simOutput=None):

    if simOutput is None:
        simOutput = buildSimulationsOutput(preprocessConfig)

    computeAOGFields(preprocessConfig, simOutput, AOG, GOR, species)
    computeFMScalingMakeGSAOGFields(preprocessConfig, simOutput, AOG, GOR, species)

#__________________________________________________

def preprocessRawDataForAllSpecies(preprocessConfig, simOutput=None):

    if simOutput is None:
        simOutput = buildSimulationsOutput(preprocessConfig)

    for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
        for species in simOutput.simConfig.speciesList[GOR]:
            preprocessRawDataForSpecies(preprocessConfig, AOG, GOR, species, simOutput)

#__________________________________________________
