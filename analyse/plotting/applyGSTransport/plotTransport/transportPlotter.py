#____________________
# transportPlotter.py
#____________________

from itertools                                      import product

from ....utils.analyse.simulation.simulationsOutput import buildSimulationsOutput
from ....utils.analyse.io.navigate                  import *
from plotTransportMap                               import plotTransportMap
from plotBackwardTransport                          import plotBackwardTransport
from plotForwardTransport                           import plotForwardTransport

#__________________________________________________

class TransportPlotter:

    def __init__(self, config):
        self.config    = config
        self.simOutput = buildSimulationsOutput(config)

    def plot(self, **kwargs):
        try:
            AOG        = kwargs['AOG']
            species    = kwargs['species']
            field      = None
            LOL        = None
            TS         = None
            configName = None

            if kwargs.has_key('field'):
                field      = kwargs['field']
            if kwargs.has_key('LOL'):
                LOL        = kwargs['LOL']
            if kwargs.has_key('TS'):
                TS         = kwargs['TS']
            if kwargs.has_key('configName'):
                configName = kwargs['configName']

            self.plotTransportForSpecies(AOG, species, field, LOL, TS, configName)
        except:
            self.plotTransportForAllSpecies()

    def plotTransportForAllSpecies(self):
        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.plotTransportForSpecies(AOG, species)

    def plotTransportForSpecies(self, AOG, species, field=None, LOL=None, TS=None, configName=None):

        (fieldList, LOLList, TSList) = self.simOutput.fieldLOLTSList(AOG, field, LOL, TS)
        if configName is None:
            configNameList = self.config.OTGS_configurationNames
        else:
            configNameList = [configName]

        for (field, LOL, TS, configName) in product(fieldList, LOLList, TSList, configNameList):

            for p1 in xrange(len(self.simOutput.procList)):
                for p0 in xrange(p1):

                    if self.config.plotForBackwardTransport:
                        plotForwardTransport(self.simOutput,
                                             configName,
                                             p0,
                                             p1,
                                             AOG,
                                             field,
                                             LOL,
                                             species,
                                             TS,
                                             self.config.plotForBackwardTransport_nLevelsGS,
                                             self.config.plotForBackwardTransport_optionInit,
                                             self.config.plotForBackwardTransport_optionFinal,
                                             self.config.plotForBackwardTransport_xLabel,
                                             self.config.plotForBackwardTransport_yLabel,
                                             self.config.plotForBackwardTransport_directionGS,
                                             self.config.plotForBackwardTransport_cmapName,
                                             self.config.plotForBackwardTransport_plotter,
                                             self.config.plotForBackwardTransport_plotterArgs,
                                             self.config.plotForBackwardTransport_extendX,
                                             self.config.plotForBackwardTransport_extendY,
                                             self.config.plotForBackwardTransport_nbrXTicks,
                                             self.config.plotForBackwardTransport_nbrYTicks,
                                             self.config.plotForBackwardTransport_nbrCTicks,
                                             self.config.plotForBackwardTransport_xTicksDecimals,
                                             self.config.plotForBackwardTransport_yTicksDecimals,
                                             self.config.plotForBackwardTransport_cTicksDecimals,
                                             self.config.plotForBackwardTransport_extensions,
                                             self.config.printIO,
                                             self.config.EPSILON)
                        
                        plotBackwardTransport(self.simOutput,
                                              configName,
                                              p0,
                                              p1,
                                              AOG,
                                              field,
                                              LOL,
                                              species,
                                              TS,
                                              self.config.plotForBackwardTransport_nLevelsGS,
                                              self.config.plotForBackwardTransport_optionInit,
                                              self.config.plotForBackwardTransport_optionFinal,
                                              self.config.plotForBackwardTransport_xLabel,
                                              self.config.plotForBackwardTransport_yLabel,
                                              self.config.plotForBackwardTransport_directionGS,
                                              self.config.plotForBackwardTransport_cmapName,
                                              self.config.plotForBackwardTransport_plotter,
                                              self.config.plotForBackwardTransport_plotterArgs,
                                              self.config.plotForBackwardTransport_extendX,
                                              self.config.plotForBackwardTransport_extendY,
                                              self.config.plotForBackwardTransport_nbrXTicks,
                                              self.config.plotForBackwardTransport_nbrYTicks,
                                              self.config.plotForBackwardTransport_nbrCTicks,
                                              self.config.plotForBackwardTransport_xTicksDecimals,
                                              self.config.plotForBackwardTransport_yTicksDecimals,
                                              self.config.plotForBackwardTransport_cTicksDecimals,
                                              self.config.plotForBackwardTransport_extensions,
                                              self.config.printIO,
                                              self.config.EPSILON)

                    if self.config.plotTransportMap:
                        plotTransportMap(self.simOutput,
                                         configName,
                                         p0,
                                         p1,
                                         AOG,
                                         field,
                                         LOL,
                                         species,
                                         TS,
                                         self.config.plotTransportMap_TmapError,
                                         self.config.plotTransportMap_TmapResolution,
                                         self.config.plotTransportMap_extensions,
                                         self.config.plotTransportMap_optionsForward,
                                         self.config.plotTransportMap_optionsBackward,
                                         self.config.plotTransportMap_extendX,
                                         self.config.plotTransportMap_extendY,
                                         self.config.plotTransportMap_nbrXTicks,
                                         self.config.plotTransportMap_nbrYTicks,
                                         self.config.plotTransportMap_xTicksDecimals,
                                         self.config.plotTransportMap_yTicksDecimals,
                                         self.config.printIO,
                                         self.config.EPSILON)

#__________________________________________________

