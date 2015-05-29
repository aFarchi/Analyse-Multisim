#___________________
# totalDeposition.py
#___________________

from ..field                    import Field
from ...filters.zeroFilterLog10 import zeroFilterLog10Coarsed

#__________________________________________________

class TotalDeposition(Field):

    def __init__(self, simOutput):
        Field.__init__(self, 'totalDeposition', [3,2], ['longitude','latitude'], simOutput)

    #_________________________

    def coarsedExtraction(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return data[:,:].transpose()

    #_________________________

    def coarsedExtractionAllIterations(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return data[:,:,:].transpose((0,2,1))

#__________________________________________________

