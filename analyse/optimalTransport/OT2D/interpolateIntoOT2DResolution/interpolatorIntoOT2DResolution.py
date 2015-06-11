#__________________________________
# interpolatorIntoOT2DResolution.py
#__________________________________

from itertools                                       import product

from interpolateIntoOT2DResolution                   import interpolateAOGFieldsIntoOT2DResolution
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *

#__________________________________________________

class InterpolatorIntoOT2DResolution:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    #_________________________

    def run(self, **kwargs):
        try:
            AOG     = kwargs['AOG']
            species = kwargs['species']
            try:
                field = kwargs['field']
            except:
                field = None
            try:
                LOL   = kwargs['LOL']
            except:
                LOL   = None

            self.interpolateIntoOT2DResolutionForSpecies(AOG, species, field, LOL)
        except:
            self.interpolateIntoOT2DResolutionForAllSpecies()

    #_________________________

    def interpolateIntoOT2DResolutionForSpecies(self, AOG, species, field=None, LOL=None):

        (fieldList, LOLList) = self.simOutput.fieldLOLList(AOG, field, LOL)

        for (field, LOL, proc) in product(fieldList, LOLList, self.simOutput.procList):
            interpolateAOGFieldsIntoOT2DResolution(self.simOutput,
                                                   AOG,
                                                   species,
                                                   field,
                                                   LOL,
                                                   proc,
                                                   self.config.OT2D_shape,
                                                   self.config.printIO)

    #_________________________
    
    def interpolateIntoOT2DResolutionForAllSpecies(self):

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.interpolateIntoOT2DResolutionForSpecies(AOG, species)

#__________________________________________________
