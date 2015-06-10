#_________
# field.py
#_________

from ..processRawData.interpolateRawData import interpolateRawData
from ..scaling.scaling                   import computeScaling
from ..timeSelection.defaultTSelect      import selectLastT

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

    def extract(self, rawData, LOL, copy=True):
        t               = self.funTSelect(rawData.shape[0])
        data            = self.extraction(rawData[t], LOL)

        defaultMaxValue = 2.0 * self.minValue
        if LOL == 'log':
            defaultMaxValue = np.log10(2.0)

        scale = computeScaling(data, self.minValue, defaultMaxValue)

        if copy:
            return (data.copy(), scale)
        else:
            return (data, scale)

    #_________________________

    def extractAllIterations(self, rawData, LOL, copy=True):
        return self.extractionAllIterations(rawData, LOL, copy)

    #_________________________

    def removeFilter(self, data, LOL):
        if LOL == 'lin':
            mini = self.minValue
        elif LOL == 'log':
            mini = 0.0

        return np.maximum(data, mini)

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
