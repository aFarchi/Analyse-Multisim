#___________________
# totalDeposition.py
#___________________

from ..field                    import Field
from ...filters.zeroFilterLog10 import zeroFilterLog10

#__________________________________________________

class TotalDeposition(Field):

    def __init__(self, simOutput):
        Field.__init__(self, 'totalDeposition', [3,2], ['longitude','latitude'], simOutput)

    #_________________________

    def extraction(self, rawData, LOL):
        data = zeroFilterLog10(rawData,self.minValue, LOL)
        return ( data[:,:].transpose() )

    #_________________________

    def extractionAllIterations(self, rawData, LOL):
        data = zeroFilterLog10(rawData,self.minValue, LOL)
        return ( data[:,:,:].transpose((0,2,1)) )

#__________________________________________________

