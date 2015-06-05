#___________________________
# plotFieldsConfiguration.py
#___________________________

from fieldsPlotter                               import FieldsPlotter
from ...utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class PlotFieldsConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PlotFieldsConfiguration class'

    #_________________________

    def plotter(self):
        return FieldsPlotter(self)

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

        self.addAttribute('plotFields',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_extensions',
                          defaultVal=['.pdf'],
                          attrType='list')

        self.addAttribute('plotFields_AOO',
                          defaultVal='all')

        self.addAttribute('plotFields_parallelize',
                          defaultVal='less')

        self.addAttribute('plotFields_applyGlobalScaling',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_xLabel',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_yLabel',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_cLabel',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_simLabels',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_colorBar',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_cmapName',
                          defaultVal='jet',
                          isSubAttr=[('plotFields_colorBar', True)])

        self.addAttribute('plotFields_extendX',
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotFields_extendY',
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotFields_nbrXTicks',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_nbrYTicks',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_nbrCTicks',
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotFields_xTicksDecimals',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_yTicksDecimals',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_cTicksDecimals',
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_plotter',
                          defaultVal='imshow')

        self.addAttribute('plotFields_plotterArgs',
                          defaultVal={},
                          attrType='dict')

        self.addAttribute('plotFields_order',
                          defaultVal='horizontalFirst')

        self.addAttribute('plotFields_extendDirection',
                          defaultVal='vertical')

#__________________________________________________
