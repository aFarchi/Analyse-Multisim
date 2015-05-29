#_____________
# airColumn.py
#_____________

import numpy as np

from ..field                    import Field
from ...filters.zeroFilterLog10 import zeroFilterLog10Coarsed

#__________________________________________________

class AirColumn(Field):

    def __init__(self, simOutput):
        Field.__init__(self, 'airColumn', [3,2], ['longitude','latitude'], simOutput)
        self.weights = np.diff(simOutput.levels)

    #_________________________

    def coarsedExtraction(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return np.average(data[:,:,:], axis=0, weights=self.weights).transpose()
        
    #_________________________

    def coarsedExtractionAllIterations(self, rawData, lol, coarseFactor):
        data = zeroFilterLog10Coarsed(rawData, self.minValue, lol, coarseFactor)
        return np.average(data[:,:,:,:], axis=1, weights=self.weights).transpose((0,2,1))
                                    
#__________________________________________________
