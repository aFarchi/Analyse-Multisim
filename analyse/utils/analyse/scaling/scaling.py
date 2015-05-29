#___________
# scaling.py
#___________

import numpy as np
from itertools            import product

from ...path.absolutePath import *

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

def computeScaling(matrix):
    scaling      = Scaling()
    scaling.mean = matrix.mean()
    scaling.var  = matrix.var()

    mini         = matrix.min()
    maxi         = matrix.max()
    extent       = maxi - mini

    if extent <= 0.0:
        extent = abs(mini)
        maxi   = mini + extent

    if extent == 0.0: # in case we are with a log scale and there is nothing
        extent = 1.0
        maxi   = 1.0

    scaling.mini = mini - 0.001 * extent
    scaling.maxi = maxi + 0.001 * extent
    
    return scaling

#__________________________________________________

def mergeScalings(scalings, maximums, fieldList, procList):

    mergedScalings = {}

    for field in fieldList:    
        mergedScalings[field] = {}
    
        for lol in ['lin','log']:
            meanMeans     = 0.
            geomMeanMeans = 1.
            meanVars      = 0.

            mini = scalings[lol][field][procList[0]].mini
            maxi = scalings[lol][field][procList[0]].maxi
            
            for proc in procList:
                meanMeans     += scalings[lol][field][proc].mean
                geomMeanMeans *= scalings[lol][field][proc].mean
                meanVars      += scalings[lol][field][proc].var

                mini = min( mini , scalings[lol][field][proc].mini )
                maxi = max( maxi , scalings[lol][field][proc].maxi )
                
            meanMeans    /= len(procList)
            geomMeanMeans = np.power(max(geomMeanMeans, 0.0), 1./len(procList))
            meanVars     /= len(procList)

            scale                      = Scaling()
            scale.mini                 = mini
            scale.maxi                 = maxi
            scale.meanMeans            = meanMeans
            scale.geomMeanMeans        = geomMeanMeans
            scale.meanVars             = meanVars
            scale.sumMaximum           = maximums[lol][field].sum()
            mergedScalings[field][lol] = scale

    return mergedScalings

#__________________________________________________

def initScalingMaximum(fieldList):
    scaling = {}
    maximum = {}
    for lol in ['lin','log']:
        scaling[lol] = {}
        maximum[lol] = {}
        for field in fieldList:
            scaling[lol][field] = {}
    return (scaling, maximum)

#__________________________________________________

def writeScaling(scaling, species, AOG, fieldList, outputDir, sessionName, printIO=False):

    for (field, lol) in product(fieldList, ['lin','log']):
        fn    = fileScaling(outputDir, sessionName, AOG, field.name, lol, species)
        array = scalingToArray(scaling[field][lol])
        if printIO:
            print ('Writing '+fn+' ...')
        np.save(fn, array)

#__________________________________________________
