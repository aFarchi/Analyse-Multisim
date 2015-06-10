#___________________________
# preprocessConfiguration.py
#___________________________

from preprocessRawData.rawDataPreprocessor      import RawDataPreprocessor
from ..utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class PreprocessConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)
        self.xTSelect = self.preprocessRawData_xTSelect

    #_________________________

    def __repr__(self):
        return 'PreprocessConfiguration class'            

    #_________________________

    def process(self):
        return RawDataPreprocessor(self)
                        
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

        #_______________

        self.addAttribute('preprocessRawData_bigMemory', 
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('preprocessRawData_xTSelect', 
                          defaultVal=1.0,
                          attrType='float')

        self.addAttribute('preprocessRawData_nLevelsFM', 
                          defaultVal=10,
                          attrType='int')

        self.addAttribute('preprocessRawData_nLevelsGrayScale', 
                          defaultVal=50,
                          attrType='int')

#__________________________________________________
