#____________________________
# simulationsConfiguration.py
#____________________________

from datetime             import datetime
from datetime             import timedelta
from ...path.absolutePath import *

#__________________________________________________

def catchSimConfig(outputDir, sessionName):
    return SimulationsConfiguration(configDir(outputDir, sessionName))

#__________________________________________________

class SimulationsConfiguration:

    def __init__(self, configDir=None):
        self.speciesList                    = {}
        self.speciesList['gaz']             = []
        self.speciesList['radios']          = []

        self.speciesBinList                 = {}
        self.speciesBinList['gaz']          = {}
        self.speciesBinList['radios']       = {}

        self.rawShapes                      = {}
        self.rawShapes['gaz']               = {}
        self.rawShapes['gaz']['air/']       = None
        self.rawShapes['gaz']['ground/']    = None
        self.rawShapes['radios']            = {}
        self.rawShapes['radios']['air/']    = None
        self.rawShapes['radios']['ground/'] = None

        try:
            self.initFromFiles(configDir)
        except:
            self.defaultInit()

    #_________________________

    def initFromFiles(self, configDir):
        # STILL NEED TO WRITE THIS FUNCTION
        raise ValueError('Not implemented')

    #_________________________

    def defaultInit(self):
        #self.speciesList['gaz']                = ['I2']
        self.speciesList['radios']             = ['Cs137']
        
        #self.speciesBinList['gaz']['I2']       = ['I2']
        self.speciesBinList['radios']['Cs137'] = ['Cs137_0','Cs137_1','Cs137_2','Cs137_3','Cs137_4']
                
        self.rawShapes['gaz']['air/']          = (83,15,120,120)
        self.rawShapes['gaz']['ground/']       = (500,1,120,120)
        self.rawShapes['radios']['air/']       = (500,15,120,120)
        self.rawShapes['radios']['ground/']    = (500,1,120,120)
        
        self.deltaT                            = 3600.

        self.xmin                              = 137.53
        self.xmax                              = 143.53

        self.ymin                              = 34.72
        self.ymax                              = 40.72

        self.zmin                              = 34.72
        self.zmax                              = 40.72

        self.tmin                              = datetime(2011, 03, 11, 0)
        self.tmax                              = self.tmin + timedelta(seconds=3000*600)
                        
#__________________________________________________
