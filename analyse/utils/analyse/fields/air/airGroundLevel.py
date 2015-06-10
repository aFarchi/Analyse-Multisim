#__________________
# airGroundLevel.py
#__________________

from ..field                    import Field
from ...filters.zeroFilterLog10 import zeroFilterLog10

#__________________________________________________

class AirGroundLevel(Field):

    def __init__(self, simOutput):
        Field.__init__(self, 'airGroundLevel', [3,2], ['longitude','latitude'], simOutput)

    #_________________________

    def extraction(self, rawData, LOL):
        data = zeroFilterLog10(rawData,self.minValue, LOL)
        return ( data[0,:,:].transpose() )

    #_________________________

    def extractionAllIterations(self, rawData, LOL):
        data = zeroFilterLog10(rawData,self.minValue, LOL)
        return ( data[:,0,:,:].transpose((0,2,1)) )

#__________________________________________________
