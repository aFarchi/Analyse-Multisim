#___________________________________
# statisticalAnalyseConfiguration.py
#___________________________________

from analyser                                   import Analyser
from ..utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class StatisticalAnalyseConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'StatisticalAnalyseConfiguration class'            

    #_________________________

    def analyser(self):
        return Analyser(self)
                        
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

        self.addAttribute('statisticalAnalyse_parallelize',
                          defaultVal='more')

        self.addAttribute('statisticalAnalyse_nLevelsAlpha',
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('statisticalAnalyse_chooseScaling',
                          defaultVal='mean')

#__________________________________________________
