#__________________
# airGroundLevel.py
#__________________

from ..field                    import Field
from ...filters.zeroFilterLog10 import zeroFilterLog10Coarsed

#__________________________________________________

class AirGroundLevel(Field):

    def __init__(self, simOutput):
        Field.__init__(self, 'airGroundLevel', [3,2], ['longitude','latitude'], simOutput)

    #_________________________

    def coarsedExtraction(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return data[0,:,:].transpose()

    #_________________________

    def coarsedExtractionAllIterations(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return data[:,0,:,:].transpose((0,2,1))

#__________________________________________________
