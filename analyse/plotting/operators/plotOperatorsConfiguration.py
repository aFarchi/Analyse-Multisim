#______________________________
# plotOperatorsConfiguration.py
#______________________________

from plotOperators.operatorsPlotter              import OperatorsPlotter
from ...utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class PlotOperatorsConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PlotOperatorsConfiguration class'

    #_________________________

    def plotter(self):
        return OperatorsPlotter(self)

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

        self.addAttribute('preprocessRawData_nLevelsFM',
                          defaultVal=10,
                          attrType='int')

        self.addAttribute('statisticalAnalyse_nLevelsAlpha',
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('OTGS_configurationNames',
                          defaultVal=['adr3'],
                          attrType='list')

        self.addAttribute('OT2D_configurationNames',
                          defaultVal=['adr3'],
                          attrType='list')
                         
        #_______________

        self.addAttribute('plotOperators_parallelize',
                          defaultVal='less')
                          
        self.addAttribute('plotOperators_extensions',
                          defaultVal=['.pdf'],
                          attrType='list')
        
        self.addAttribute('plotOperators_cmapName',
                          defaultVal='gray')

#__________________________________________________
