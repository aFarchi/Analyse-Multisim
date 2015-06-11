#_____________________
# OTGSConfiguration.py
#_____________________

from ...utils.configuration.defaultConfiguration                  import DefaultConfiguration
from interpolateIntoOTGSResolution.interpolatorIntoOTGSResolution import InterpolatorIntoOTGSResolution
from mergeOTGSResults.OTGSResultsMerger                           import OTGSResultsMerger
from applyOTGS.GSTransportApplier                                 import GSTransportApplier

#__________________________________________________

class OTGSConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'OTGSConfiguration class'            

    #_________________________

    def interpolatorIntoOTGSResolution(self):
        return InterpolatorIntoOTGSResolution(self)

    #_________________________

    def OTGSResultMerger(self):
        return OTGSResultsMerger(self)

    #_________________________

    def OTGSTransportApplier(self):
        return GSTransportApplier(self)

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

        self.addAttribute('OTGS_resolution',
                          defaultVal=31,
                          attrType='int')

        self.addAttribute('OTGS_interpolateIntoOTGSResolution_parallelize',
                          defaultVal='more')

        self.addAttribute('OTGS_mergeOTGSResults_parallelize',
                          defaultVal='more')

        #_______________

        self.addAttribute('OTGS_configurationNames',
                          defaultVal=['adr3'],
                          attrType='list')

        self.addAttribute('OTGS_algorithmParametersFiles',
                          defaultVal={'adr3':'OTGSAlgorithmParameters.cfg'},
                          attrType='dict')

        self.addAttribute('OTGS_plottingParametersFiles',
                          defaultVal={'adr3':'OTGSPlottingParameters.cfg'},
                          attrType='dict')

        self.addAttribute('OTGS_plottingParametersFileAllConfig',
                          defaultVal='OTGSPlottingParameters.cfg')

        #_______________

        self.addAttribute('OTGS_applyOTGS_Error',
                          defaultVal=0.001,
                          attrType='float')

        self.addAttribute('OTGS_applyOTGS_parallelize',
                          defaultVal='more')

#__________________________________________________
