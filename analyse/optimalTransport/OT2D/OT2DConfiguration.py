#_____________________
# OT2DConfiguration.py
#_____________________

from ...utils.configuration.defaultConfiguration import DefaultConfiguration

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
        
        while(len(self.preprocessRawData_analyseShape) < 4):
            self.preprocessRawData_analyseShape.append(1)

        self.preprocessRawData_analyseShape = tuple(self.preprocessRawData_analyseShape[0:4])

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

        self.addAttribute('preprocessRawData_analyseShape', 
                          defaultVal=[1,1,32,32],
                          attrType='list')

        self.addAttribute('OT2D_timeResFunction', 
                          defaultVal='min')

        self.addAttribute('OT2D_algoNames', 
                          defaultVal=['adr3'],
                          attrType='list')

        self.addAttribute('OT2D_dynamics', 
                          defaultVal={'adr':'1', 'pd':'1', 'adr3':'4'},
                          attrType='dict')

        self.addAttribute('OT2D_normType', 
                          defaultVal={'adr':'0', 'pd':'0', 'adr3':'-1'},
                          attrType='dict')

        self.addAttribute('OT2D_iterTarget', 
                          defaultVal={'adr':'1000', 'pd':'1000', 'adr3':'1000'},
                          attrType='dict')

        self.addAttribute('OT2D_nModPrint', 
                          defaultVal={'adr':'200', 'pd':'200', 'adr3':'200'},
                          attrType='dict')

        self.addAttribute('OT2D_nModWrite', 
                          defaultVal={'adr':'10', 'pd':'10', 'adr3':'10'},
                          attrType='dict')

        self.addAttribute('OT2D_initial', 
                          defaultVal={'adr':'1', 'pd':'1', 'adr3':'1'},
                          attrType='dict')

        self.addAttribute('OT2D_initialID', 
                          defaultVal={'adr':'./', 'pd':'./', 'adr3':'./'},
                          attrType='dict')

        self.addAttribute('OT2D_gamma', 
                          defaultVal='0.013333333')

        self.addAttribute('OT2D_alpha', 
                          defaultVal='1.998')

        self.addAttribute('OT2D_theta', 
                          defaultVal='1.')
 
        self.addAttribute('OT2D_sigma', 
                          defaultVal='85.')
        
        self.addAttribute('OT2D_tau', 
                          defaultVal='0.0116470588235294')

        self.addAttribute('OT2D_gamma3', 
                          defaultVal='0.013333333')

        self.addAttribute('OT2D_alpha3', 
                          defaultVal='1.998')
        
        self.addAttribute('OT2D_omega1', 
                          defaultVal='0.33')

        self.addAttribute('OT2D_omega2', 
                          defaultVal='0.33')

        self.addAttribute('OT2D_omega3', 
                          defaultVal='0.34')

        self.addAttribute('OT2D_plottingParametersFile',
                          defaultVal='OT2DPlottingParameters.cfg')

#__________________________________________________
