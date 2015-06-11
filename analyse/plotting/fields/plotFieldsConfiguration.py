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

        #_______________

        self.addAttribute('preprocessRawData_nLevelsGrayScale',
                          defaultVal=1000,
                          attrType='int')

        #_______________

        self.addAttribute('plotFields',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_extensions',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=['.pdf'],
                          attrType='list')
        
        self.addAttribute('plotFields_AOO',
                          isSubAttr=[('plotFields', True)],
                          defaultVal='all')

        self.addAttribute('plotFields_parallelize',
                          isSubAttr=[('plotFields', True)],
                          defaultVal='less')

        self.addAttribute('plotFields_applyGlobalScaling',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_xLabel',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_yLabel',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_cLabel',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_simLabels',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_colorBar',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFields_cmapName',
                          isSubAttr=[('plotFields', True)],
                          defaultVal='jet')

        self.addAttribute('plotFields_extendX',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotFields_extendY',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotFields_nbrXTicks',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_nbrYTicks',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_nbrCTicks',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotFields_xTicksDecimals',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_yTicksDecimals',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_cTicksDecimals',
                          isSubAttr=[('plotFields', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFields_plotter',
                          isSubAttr=[('plotFields', True)],
                          defaultVal='imshow')

        self.addAttribute('plotFields_plotterArgs',
                          isSubAttr=[('plotFields', True)],
                          defaultVal={},
                          attrType='dict')

        self.addAttribute('plotFields_order',
                          isSubAttr=[('plotFields', True)],
                          defaultVal='horizontalFirst')

        self.addAttribute('plotFields_extendDirection',
                          isSubAttr=[('plotFields', True)],
                          defaultVal='horizontal')

        #_______________

        self.addAttribute('plotFieldsAttachGrayScale',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFieldsAttachGrayScale_extensions',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=['.pdf'],
                          attrType='list')

        self.addAttribute('plotFieldsAttachGrayScale_AOO',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='one')

        self.addAttribute('plotFieldsAttachGrayScale_parallelize',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='less')

        self.addAttribute('plotFieldsAttachGrayScale_simLabels',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFieldsAttachGrayScale_xLabel',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFieldsAttachGrayScale_yLabel',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotFieldsAttachGrayScale_order',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='horizontalFirst')

        self.addAttribute('plotFieldsAttachGrayScale_extendDirection',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='horizontal')

        self.addAttribute('plotFieldsAttachGrayScale_plotter',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='imshow')

        self.addAttribute('plotFieldsAttachGrayScale_plotterArgs',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal={},
                          attrType='dict')

        self.addAttribute('plotFieldsAttachGrayScale_extendX',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotFieldsAttachGrayScale_extendY',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotFieldsAttachGrayScale_nbrXTicks',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFieldsAttachGrayScale_nbrYTicks',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFieldsAttachGrayScale_nbrCTicks',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotFieldsAttachGrayScale_xTicksDecimals',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFieldsAttachGrayScale_yTicksDecimals',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFieldsAttachGrayScale_cTicksDecimals',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotFieldsAttachGrayScale_cmapName',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='jet')

        self.addAttribute('plotFieldsAttachGrayScale_scaleGS',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal=False,
                          attrType='bool')

        self.addAttribute('plotFieldsAttachGrayScale_extendDirectionGS',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='vertical')

        self.addAttribute('plotFieldsAttachGrayScale_options',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal={'Threshold':'k--','NoThreshold':'k-'},
                          attrType='dict')

        self.addAttribute('plotFieldsAttachGrayScale_directionGS',
                          isSubAttr=[('plotFieldsAttachGrayScale', True)],
                          defaultVal='horizontal')

#__________________________________________________
