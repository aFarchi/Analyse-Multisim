#_____________________
# OTGSConfiguration.py
#_____________________

from ...utils.configuration.defaultConfiguration                  import DefaultConfiguration
from interpolateIntoOTGSResolution.interpolatorIntoOTGSResolution import InterpolatorIntoOTGSResolution

#__________________________________________________

class OTGSConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PreprocessConfiguration class'            

    #_________________________

    def checkAttributes(self):
        DefaultConfiguration.checkAttributes(self)
        
    #_________________________

    def interpolatorIntoOTGSResolution(self):
        return InterpolatorIntoOTGSResolution(self)

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

        #_________________________

        self.addAttribute('OTGS_resolution',
                          defaultVal=31,
                          attrType='int')

        self.addAttribute('OTGS_interpolateIntoOTGSResolution',
                          defaultVal=True,
                          attrType='bool')

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

#__________________________________________________
