#__________________________________
# interpolatorIntoOTGSResolution.py
#__________________________________

from itertools                                       import product

from interpolateIntoOTGSResolution                   import interpolateProcPreprocessedDieldGSIntoOTGSResolution
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
            GOR     = kwargs['GOR']
            species = kwargs['species']
            try:
                field = kwargs['field']
            except:
                field = None
            try:
                LOL   = kwargs['LOL']
            except:
                LOL   = None
            try:
                TS    = kwargs['TS']
            except:
                TS    = None
            
            self.interpolateIntoOTGSResolutionForSpecies(AOG, GOR, species, field, LOL, TS)
        except:
            self.interpolateIntoOTGSResolutionForAllSpecies()

    #_________________________

    def interpolateIntoOTGSResolutionForSpecies(self, AOG, GOR, species, field=None, LOL=None, TS=None):

        (fieldList, LOLList, TSList) = self.simOutput.fieldLOLTSList(AOG, field, LOL, TS)

        for (field, LOL, TS, proc) in product(fieldList, LOLList, TSList, self.simOutput.procList):
            interpolateProcPreprocessedDieldGSIntoOTGSResolution(self.simOutput,
                                                                 AOG,
                                                                 species,
                                                                 field,
                                                                 LOL,
                                                                 TS,
                                                                 proc,
                                                                 self.config.OTGS_resolution,
                                                                 self.config.printIO)

    #_________________________
    
    def interpolateIntoOTGSResolutionForAllSpecies(self):

        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.interpolateIntoOTGSResolutionForSpecies(AOG, GOR, species)

#__________________________________________________
