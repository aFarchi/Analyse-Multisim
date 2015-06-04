#_____________________
# OT2DConfiguration.py
#_____________________

from ...utils.configuration.defaultConfiguration                  import DefaultConfiguration
from interpolateIntoOT2DResolution.interpolatorIntoOT2DResolution import InterpolatorIntoOT2DResolution

#__________________________________________________

class OT2DConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PreprocessConfiguration class'            

    #_________________________

    def checkAttributes(self):
        DefaultConfiguration.checkAttributes(self)
        self.OT2D_shape = (self.OT2D_Nt, self.OT2D_Nz, self.OT2D_Ny, self.OT2D_Nx)

    #_________________________

    def interpolatorIntoOT2DResolution(self):
        return InterpolatorIntoOT2DResolution(self)

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

        self.addAttribute('OT2D_Nx',
                          defaultVal=31,
                          attrType='int')

        self.addAttribute('OT2D_Ny',
                          defaultVal=31,
                          attrType='int')

        self.addAttribute('OT2D_Nz',
                          defaultVal=31,
                          attrType='int')

        self.addAttribute('OT2D_Nt',
                          defaultVal=31,
                          attrType='int')

        self.addAttribute('OT2D_timeResFunction', 
                          defaultVal='min')

        self.addAttribute('OT2D_interpolateIntoOT2DResolution',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('OT2D_configurationNames',
                          defaultVal=['adr3'],
                          attrType='list')

        self.addAttribute('OT2D_algorithmParametersFiles',
                          defaultVal={'adr3':'OT2DAlgorithmParameters.cfg'},
                          attrType='dict')

        self.addAttribute('OT2D_plottingParametersFiles',
                          defaultVal={'adr3':'OT2DPlottingParameters.cfg'},
                          attrType='dict')

        self.addAttribute('OT2D_plottingParametersFileAllConfig',
                          defaultVal='OT2DPlottingParameters.cfg')

#__________________________________________________
