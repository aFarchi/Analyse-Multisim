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

        #_______________

        self.addAttribute('plotSimulationsField',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_extensions',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=['.pdf'],
                          attrType='list')

        self.addAttribute('plotSimulationsField_AOO',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal='all')

        self.addAttribute('plotSimulationsField_parallelize',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal='less')

        self.addAttribute('plotSimulationsField_xLabel',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_yLabel',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_cLabel',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_simLabels',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_timeTextPBar',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_colorBar',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotSimulationsField_cmapName',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal='jet')

        self.addAttribute('plotSimulationsField_extendX',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotSimulationsField_extendY',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotSimulationsField_nbrXTicks',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_nbrYTicks',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_nbrCTicks',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotSimulationsField_xTicksDecimals',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_yTicksDecimals',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_cTicksDecimals',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotSimulationsField_plotter',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal='imshow')

        self.addAttribute('plotSimulationsField_plotterArgs',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal={},
                          attrType='dict')

        self.addAttribute('plotSimulationsField_order',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal='horizontalFirst')

        self.addAttribute('plotSimulationsField_extendDirection',
                          isSubAttr=[('plotSimulationsField', True)],
                          defaultVal='vertical')

#__________________________________________________
