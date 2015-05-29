#_____________
# airColumn.py
#_____________

import numpy as np

from ..field                    import Field
from ...io.readLists            import catchLevelsFromFile
from ...filters.zeroFilterLog10 import zeroFilterLog10Coarsed

#__________________________________________________

class AirColumn(Field):

    def __init__(self, minValues=None, funTSelect=None, levels=None):

        if minValues is None:
            minValue = 1.e-5
        else:
            minValue = minValues['airColumn']
                                        
        Field.__init__(self, 'airColumn', [3,2], ['longitude','latitude'], minValue, funTSelect)

        if levels is None:
            self.weights = None
        else:
            self.weights = np.diff(levels)

    #_________________________

    def coarsedExtraction(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        if self.weights is None:
            data = np.average(data[:,:,:], axis=0).transpose()
        else:
            data = np.average(data[:,:,:], axis=0, weights=self.weights).transpose()
        return data

    #_________________________

    def coarsedExtractionAllIterations(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        if self.weights is None:
            data = np.average(data[:,:,:,:], axis=1).transpose((0,2,1))
        else:
            data = np.average(data[:,:,:,:], axis=1, weights=self.weights).transpose((0,2,1))
        return data

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
