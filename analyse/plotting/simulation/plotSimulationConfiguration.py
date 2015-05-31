#_______________________________
# plotSimulationConfiguration.py
#_______________________________

from simulationsPlotter                          import SimulationsPlotter
from ...utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class PlotSimulationConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PlotSimulationConfiguration class'

    #_________________________

    def plotter(self):
        return SimulationsPlotter(self)

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

        self.addAttribute('extensions',
                          defaultVal=['.pdf'],
                          attrType='list')

        self.addAttribute('plotSimulationsField',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_AOO',
                          defaultVal='all')

        self.addAttribute('plotSimulationsField_parallelize',
                          defaultVal='less')

        self.addAttribute('plotSimulationsField_xLabel',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_yLabel',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_cLabel',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_simLabels',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_timeTextPBar',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_colorBar',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_cmapName',
                          defaultVal='jet',
                          isSubAttr=[('plotSimulationsField_colorBar', True)])

        self.addAttribute('plotSimulationsField_extendX',
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotSimulationsField_extendY',
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotSimulationsField_nbrXTicks',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_nbrYTicks',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_nbrCTicks',
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotSimulationsField_xTicksDecimals',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_yTicksDecimals',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_cTicksDecimals',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_plotter',
                          defaultVal='imshow')

        self.addAttribute('plotSimulationsField_plotterArgs',
                          defaultVal={},
                          attrType='dict')

        self.addAttribute('plotSimulationsField_order',
                          defaultVal='horizontalFirst')

        self.addAttribute('plotSimulationsField_extendDirection',
                          defaultVal='vertical')

#__________________________________________________
