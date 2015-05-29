#___________________________
# preprocessConfiguration.py
#___________________________

#from preprocessRawData          import preprocessRawDataForSpecies
#from preprocessRawData          import preprocessRawDataForAllSpecies
#from preprocessRawDataBigMemory import preprocessRawDataForSpeciesBigMemory
#from preprocessRawDataBigMemory import preprocessRawDataForAllSpeciesBigMemory

from ..utils.configuration.defaultConfiguration import DefaultConfiguration

#__________________________________________________

class PreprocessConfiguration(DefaultConfiguration):

    def __init__(self, configFile=None):
        DefaultConfiguration.__init__(self, configFile)

    #_________________________

    def __repr__(self):
        return 'PreprocessConfiguration class'            

    #_________________________

    def checkAttributes(self):
        DefaultConfiguration.checkAttributes(self)
        
        while(len(self.analyseShape) < 4):
            self.analyseShape.append(1)

        self.analyseShape = tuple(self.analyseShape[0:4])

    #_________________________

    def runAll(self):
        if self.bigMemory == 1:
            preprocessRawDataForAllSpeciesBigMemory(self.outputDir,
                                                    self.sessionName,
                                                    self.xTSelect,
                                                    self.analyseShape,
                                                    self.nLevelsAnalyse,
                                                    self.printIO)
        else:
            preprocessRawDataForAllSpecies(self.outputDir,
                                           self.sessionName,
                                           self.xTSelect,
                                           self.analyseShape,
                                           self.nLevelsAnalyse,
                                           self.printIO)
                        
    #_________________________

    def runOne(self, AOG, GOR, species):
        if self.bigMemory == 1:
            preprocessRawDataForSpeciesBigMemory(self.outputDir,
                                                 self.sessionName,
                                                 self.xTSelect,
                                                 self.analyseShape,
                                                 self.nLevelsAnalyse,
                                                 AOG,
                                                 GOR,
                                                 species,
                                                 self.printIO)
        else:
            preprocessRawDataForSpecies(self.outputDir,
                                        self.sessionName,
                                        self.xTSelect,
                                        self.analyseShape,
                                        self.nLevelsAnalyse,
                                        AOG,
                                        GOR,
                                        species,
                                        self.printIO)

    #_________________________

    def writeConfig(self, fileName):
        f = open(fileName, 'w')
        f.write('outputDir      = '+self.outputDir+'\n')
        f.write('sessionName    = '+self.sessionName+'\n')
        f.write('xTSelect       = '+str(self.xTSelect)+'\n')
        for shape in self.analyseShape:
            f.write('analyseShape   = int : '+str(shape)+'\n')
        f.write('nLevelsAnalyse = '+str(self.nLevelsAnalyse)+'\n')
        f.write('printIO        = '+str(self.printIO)+'\n')
        f.write('bigMemory      = '+str(self.bigMemory)+'\n')
        f.close()

    #_________________________

    def defaultAttributes(self):
        DefaultConfiguration.defaultAttributes(self)

        self.addAttribute('outputDir',
                          defaultVal='/cerea_raid/users/farchia/Fukushima-multisim/output/')

        self.addAttribute('sessionName',
                          defaultVal='sim-test/')

        self.addAttribute('workName',
                          defaultVal='analyse/')

        self.addAttribute('xTSelect', 
                          defaultVal=1.0,
                          attrType='float')

        self.addAttribute('analyseShape', 
                          defaultVal=[1,1,32,32],
                          attrType='list')

        self.addAttribute('nLevelsAnalyse', 
                          defaultVal=30,
                          attrType='int')

        self.addAttribute('printIO',
                          defaultVal=True,
                          attrType='bool')

        self.addAttribute('bigMemory', 
                          defaultVal=True,
                          attrType='bool')
                                                
#__________________________________________________
