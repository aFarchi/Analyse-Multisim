#___________________________
# preprocessConfiguration.py
#___________________________

from preprocessor                               import Preprocessor
from ..utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class PreprocessConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PreprocessConfiguration class'            

    #_________________________

    def checkAttributes(self):
        DefaultConfiguration.checkAttributes(self)
        
        while(len(self.preprocessRawData_analyseShape) < 4):
            self.preprocessRawData_analyseShape.append(1)

        self.preprocessRawData_analyseShape = tuple(self.preprocessRawData_analyseShape[0:4])

    #_________________________

    def process(self):
        return Preprocessor(self)
                        
    #_________________________

    def defaultAttributes(self):
        DefaultConfiguration.defaultAttributes(self)

        self.addAttribute('outputDir',
                          defaultVal='/cerea_raid/users/farchia/Fukushima-multisim/output/')

        self.addAttribute('sessionName',
                          defaultVal='sim-test/')

        self.addAttribute('workName',
                          defaultVal='analyse/')

        self.addAttribute('printIO',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('EPSILON',
                          defaultVal=1.e-8,
                          attrType='float')

        self.addAttribute('preprocessRawData', 
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('preprocessRawData_bigMemory', 
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('preprocessRawData_xTSelect', 
                          defaultVal=1.0,
                          attrType='float')

        self.addAttribute('preprocessRawData_analyseShape', 
                          defaultVal=[1,1,32,32],
                          attrType='list')

        self.addAttribute('preprocessRawData_nLevelsAnalyse', 
                          defaultVal=30,
                          attrType='int')

#__________________________________________________
