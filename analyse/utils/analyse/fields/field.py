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

    def extract(self, rawData, LOL, TS):
        t     = self.funTSelect(rawData.shape[0])
        data  = self.extraction(rawData[t], LOL, TS)
        scale = computeScaling(data)

        if LOL == 'lin':
            scale.mini = self.minValue
            if scale.maxi <= self.minValue:
                scale.maxi = 2 * self.minValue

        elif LOL == 'log':
            scale.mini = 0.0
            if scale.maxi <= 0.0:
                scale.maxi = 1.0

        return (data, scale)

    #_________________________

    def extractAllIterations(self, rawData, LOL, TS):
        return self.extractionAllIterations(rawData, LOL, TS)

    #_________________________

    def computeGrayScale(self, data, mini, maxi, nLevels, threshold=True):
        if threshold:
            threshold = self.minValue
        else:
            threshold = None
        return makeGrayScale(data, mini=mini, maxi=maxi, nLevels=nLevels, threshold=threshold)

    #_________________________

    def computeFMScaling(self, rawData, LOL, mini, maxi, nLevels):
        t    = self.funTSelect(rawData.shape[0])
        data = self.extraction(rawData[t], LOL, TS) 
        return computeFMScaling(data, mini=mini, maxi=maxi, nLevels=nLevels)

    #_________________________

    #def computeFMScalingMakeGrayScale(self, rawData, LOL, TS, mini, maxi, nLevels):
    #    t         = self.funTSelect(rawData.shape[0])
    #    data      = self.extraction(rawData[t], lol, 0.5)

    #    FMScaling = computeFMScaling(data, mini=mini, maxi=maxi, nLevels=nLevels)
    #    GSNT      = self.computeGrayScale(data, mini, maxi, nLevels, False)
    #    GST       = self.computeGrayScale(data, mini, maxi, nLevels, True)

    #    return (FMScaling, GSNT, GST)

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
