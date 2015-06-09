#______________________________
# plotTransportConfiguration.py
#______________________________

from plotTransport.transportPlotter              import TransportPlotter
from ...utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class PlotTransportConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PlotFieldsConfiguration class'

    #_________________________

    def plotter(self):
        return TransportPlotter(self)

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
        
        self.addAttribute('OTGS_configurationNames',
                          defaultVal=['pd'],
                          attrType='list')

        #_______________

        self.addAttribute('plotApplyGSTransport_parallelize',
                          defaultVal='more')

        self.addAttribute('plotForBackwardTransport',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotForBackwardTransport_nLevelsGS',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=100,
                          attrType='int')

        self.addAttribute('plotForBackwardTransport_optionInit',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal='g-')

        self.addAttribute('plotForBackwardTransport_optionFinal',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal='r-')

        self.addAttribute('plotForBackwardTransport_xLabel',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotForBackwardTransport_yLabel',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotForBackwardTransport_directionGS',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal='horizontal')

        self.addAttribute('plotForBackwardTransport_cmapName',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal='jet')

        self.addAttribute('plotForBackwardTransport_plotter',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal='imshow')

        self.addAttribute('plotForBackwardTransport_plotterArgs',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal={},
                          attrType='dict')

        self.addAttribute('plotForBackwardTransport_extendX',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotForBackwardTransport_extendY',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotForBackwardTransport_nbrXTicks',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotForBackwardTransport_nbrYTicks',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotForBackwardTransport_nbrCTicks',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotForBackwardTransport_xTicksDecimals',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotForBackwardTransport_yTicksDecimals',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotForBackwardTransport_cTicksDecimals',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotForBackwardTransport_extensions',
                          isSubAttr=[('plotForBackwardTransport', True)],
                          defaultVal=['.pdf'],
                          attrType='list')

        #_______________

        self.addAttribute('plotTransportMap',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('plotTransportMap_TmapError',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=0.001,
                          attrType='float')

        self.addAttribute('plotTransportMap_TmapResolution',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=100,
                          attrType='int')

        self.addAttribute('plotTransportMap_optionsForward',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal='g-')

        self.addAttribute('plotTransportMap_optionsBackward',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal='r-')

        self.addAttribute('plotTransportMap_extendX',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotTransportMap_extendY',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=0.0,
                          attrType='float')

        self.addAttribute('plotTransportMap_nbrXTicks',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotTransportMap_nbrYTicks',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=5,
                          attrType='int')

        self.addAttribute('plotTransportMap_xTicksDecimals',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotTransportMap_yTicksDecimals',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=2,
                          attrType='int')

        self.addAttribute('plotTransportMap_extensions',
                          isSubAttr=[('plotTransportMap', True)],
                          defaultVal=['.pdf'],
                          attrType='list')

#__________________________________________________
