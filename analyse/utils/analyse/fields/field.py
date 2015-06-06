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

    def __init__(self, name, axes, labels, simOutput):
        self.name      = name
        self.axes      = axes
        self.labels    = labels
        self.simOutput = simOutput
        self.minValue  = simOutput.minValues[self.name]

        if simOutput.funTSelect is None:
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

    #_________________________

    def axMini(self, ax):
        dim = self.axes[ax]
        return self.simOutput.simConfig.axMinis[dim]

    #_________________________

    def axMaxi(self, ax):
        dim = self.axes[ax]
        return self.simOutput.simConfig.axMaxis[dim]

    #_________________________

    def axExtend2d(self):
        xmin  = self.axMini(0)
        ymin  = self.axMini(1)
        xmax  = self.axMaxi(0)
        ymax  = self.axMaxi(1)
        return (xmin, xmax, ymin, ymax)

    #_________________________

    def labels2d(self, xLabel, yLabel, cLabel):
        if xLabel:
            xLabel = self.labels[0]
        else:
            xLabel = ''

        if yLabel:
            yLabel = self.labels[1]
        else:
            yLabel = ''

        if cLabel:
            cLabel = self.name
        else:
            cLabel = ''

        return (xLabel, yLabel, cLabel)

#__________________________________________________
