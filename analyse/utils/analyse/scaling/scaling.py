#___________
# scaling.py
#___________

import numpy as np
from itertools     import product
from ..io.navigate import *

#__________________________________________________

class Scaling:
    pass

#__________________________________________________

def scalingToArray(scale):
    array    = np.zeros(6)
    array[0] = scale.mini
    array[1] = scale.maxi
    array[2] = scale.meanMeans
    array[3] = scale.geomMeanMeans
    array[4] = scale.meanVars
    array[5] = scale.sumMaximum
    return array

#__________________________________________________

def arrayToScaling(array):
    scale               = Scaling()
    scale.mini          = array[0]
    scale.maxi          = array[1]
    scale.meanMeans     = array[2]
    scale.geomMeanMeans = array[3]
    scale.meanVars      = array[4]
    scale.sumMaximum    = array[5]
    return scale

#__________________________________________________

def computeScaling(matrix, minValue, defaultMaxValue):
    scaling      = Scaling()
    scaling.mean = matrix.mean()
    scaling.var  = matrix.var()

    scaling.mini = minValue
    scaling.maxi = matrix.max()

    if scaling.maxi <= minValue:
        scaling.maxi = defaultMaxValue

    return scaling

#__________________________________________________

def mergeScalings(simOutput, scalings, maximums, AOG):

    mergedScalings = {}

    for field in simOutput.fieldList[AOG]:
        mergedScalings[field.name] = {}
    
        for lol in LinOrLog():
            meanMeans     = 0.
            geomMeanMeans = 1.
            meanVars      = 0.

            mini = scalings[lol][field.name][simOutput.procList[0]].mini
            maxi = scalings[lol][field.name][simOutput.procList[0]].maxi
            
            for proc in simOutput.procList:
                meanMeans     += scalings[lol][field.name][proc].mean
                geomMeanMeans *= scalings[lol][field.name][proc].mean
                meanVars      += scalings[lol][field.name][proc].var

                mini = min( mini , scalings[lol][field.name][proc].mini )
                maxi = max( maxi , scalings[lol][field.name][proc].maxi )
                
            meanMeans    /= len(simOutput.procList)
            geomMeanMeans = np.power(max(geomMeanMeans, 0.0), 1./len(simOutput.procList))
            meanVars     /= len(simOutput.procList)

            scale                           = Scaling()
            scale.mini                      = mini
            scale.maxi                      = maxi
            scale.meanMeans                 = meanMeans
            scale.geomMeanMeans             = geomMeanMeans
            scale.meanVars                  = meanVars
            scale.sumMaximum                = np.maximum(maximums[lol][field.name], 0.0).sum()
            mergedScalings[field.name][lol] = scale

    return mergedScalings

#__________________________________________________

def initScalingMaximum(simOutput, AOG):
    scaling = {}
    maximum = {}
    for lol in LinOrLog():
        scaling[lol] = {}
        maximum[lol] = {}
        for field in simOutput.fieldList[AOG]:
            scaling[lol][field.name] = {}
    return (scaling, maximum)

#__________________________________________________

def writeScaling(simOutput, scaling, species, AOG, printIO=False):

    for (field, lol) in product(simOutput.fieldList[AOG], LinOrLog()):
        fn    = simOutput.fileScalingFieldSpecies(AOG, field, lol, species)
        array = scalingToArray(scaling[field.name][lol])
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, array)

#__________________________________________________
