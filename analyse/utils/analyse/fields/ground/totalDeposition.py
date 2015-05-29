#___________________
# totalDeposition.py
#___________________

from ..field                    import Field
from ...filters.zeroFilterLog10 import zeroFilterLog10Coarsed

#__________________________________________________

class TotalDeposition(Field):

    def __init__(self, minValues=None, funTSelect=None):
        if minValues is None:
            minValue = 1.0
        else:
            minValue = minValues['totalDeposition']
        self.minValue = minValue

        Field.__init__(self, 'totalDeposition', [3,2], ['longitude','latitude'], minValue, funTSelect)

    #_________________________

    def coarsedExtraction(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return data[:,:].transpose()

    #_________________________

    def coarsedExtractionAllIterations(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return data[:,:,:].transpose((0,2,1))

    #_________________________

    def xmin(self, lists):
        return lists.xmin

    #_________________________

    def xmax(self, lists):
        return lists.xmax

    #_________________________

    def ymin(self, lists):
        return lists.ymin

    #_________________________

    def ymax(self, lists):
        return lists.ymax

#__________________________________________________

