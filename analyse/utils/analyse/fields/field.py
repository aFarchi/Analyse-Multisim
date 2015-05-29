#_________
# field.py
#_________

from ..processRawData.interpolateRawData    import interpolateRawData
from ..scaling.scaling                      import computeScaling
from ..scaling.fmScaling                    import computeFMScaling
from ..scaling.grayScale                    import makeGrayScale
from ..timeSelection.defaultTSelect         import selectLastT

#__________________________________________________

class Field:

    def __init__(self, name, axes, labels, minValue, funTSelect=None):
        self.name     = name
        self.axes     = axes
        self.labels   = labels
        self.minValue = minValue

        if funTSelect is None:
            self.funTSelect = selectLastT
        else:
            self.funTSelect = funTSelect

    #_________________________

    def extract(self, rawData, lol):
        t     = self.funTSelect(rawData.shape[0])
        data  = self.coarsedExtraction(rawData[t], lol, 1.0)
        scale = computeScaling(data)
        return (data, scale)

    #_________________________

    def extractAllIterations(self, rawData, lol):
        return self.coarsedExtractionAllIterations(rawData, lol, 1.0)

    #_________________________

    def computeFMScalingMakeGrayScale(self, rawData, lol, mini, maxi, nLevels):
        t         = self.funTSelect(rawData.shape[0])
        data      = self.coarsedExtraction(rawData[t], lol, 0.5)

        FMScaling = computeFMScaling(data, mini=mini, maxi=maxi, nLevels=nLevels)
        GSNT      = makeGrayScale(data, mini=mini, maxi=maxi, nLevels=nLevels, threshold=None)
        GST       = makeGrayScale(data, mini=mini, maxi=maxi, nLevels=nLevels, threshold=self.minValue)

        return (FMScaling, GSNT, GST)

    #_________________________

    def fieldShape(self, analyseShape):
        shape = []
        for ax in self.axes:
            shape.append(analyseShape[ax])
        return tuple(shape)
        
    #_________________________

    def interpolate(self, extractedData, analyseShape):
        return interpolateRawData(extractedData, self.fieldShape(analyseShape))            

#__________________________________________________
