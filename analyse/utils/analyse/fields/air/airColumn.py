#_____________
# airColumn.py
#_____________

import numpy as np

from ..field                    import Field
from ...filters.zeroFilterLog10 import zeroFilterLog10

#__________________________________________________

class AirColumn(Field):

    def __init__(self, simOutput):
        Field.__init__(self, 'airColumn', [3,2], ['longitude','latitude'], simOutput)
        self.weights = np.diff(simOutput.levels)

    #_________________________

    def extraction(self, rawData, LOL):
        data = zeroFilterLog10(rawData, self.minValue, LOL)
        return ( np.average(data[:,:,:], axis=0, weights=self.weights).transpose() )

    #_________________________

    def extractionAllIterations(self, rawData, LOL):
        data = zeroFilterLog10(rawData,self.minValue, LOL)
        return ( np.average(data[:,:,:,:], axis=1, weights=self.weights).transpose((0,2,1)) )
                                    
#__________________________________________________
