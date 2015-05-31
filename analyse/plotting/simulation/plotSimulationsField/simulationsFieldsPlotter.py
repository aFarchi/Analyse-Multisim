#____________________________
# simulationsFieldsPlotter.py
#____________________________

from itertools                                       import product

from ....utils.analyse.processRawData.extractRawData import extractRawDataMultiProc
from ....utils.analyse.simulation.simulationsOutput  import buildSimulationsOutput
from ....utils.analyse.io.navigate                   import *
from plotSimulationsFields                           import plotFieldAllSim

#__________________________________________________

class SimulationsFieldPlotter:

    def __init__(self, plotSimOutputConfig):
        self.config    = plotSimOutputConfig
        self.simOutput = buildSimulationsOutput(plotSimOutputConfig)

    def plot(self, **kwargs):
        if self.config.plotSimulationsField:
            #try:
            if True:
                AOG       = kwargs['AOG']
                GOR       = kwargs['GOR']
                species   = kwargs['species']
                field     = None
                LOL       = None
                if kwargs.has_key('field'):
                    field = kwargs['field']
                if kwargs.has_key('LOL'):
                    LOL   = kwargs['field']
                self.plotAOGFieldsAllSim(AOG, GOR, species, field, LOL)
            #except:
            #self.plotFieldsForAllSpeciesAllSim()

    def plotFieldsForAllSpeciesAllSim(self):
        for (AOG, GOR) in product(AirOrGround(), GazOrRadios()):
            for species in self.simOutput.simConfig.speciesList[GOR]:
                self.plotAOGFieldsAllSim(AOG, GOR, species)

    def plotAOGFieldsAllSim(self, AOG, GOR, species, field=None, LOL=None):

        rawData = extractRawDataMultiProc(self.simOutput, AOG, GOR, species, self.config.printIO)

        print field
        print LOL

        if field is None:
            fieldList = self.simOutput.fieldList[AOG]
        else:
            fieldList = [field]

        if LOL is None:
            LOLList   = LinOrLog()
        else:
            LOLList   = [LOL]

        cmapName      = 'jet'
        if self.config.plotSimulationsField_colorBar:
            cmapName  = self.config.plotSimulationsField_cmapName

        for (field, LOL) in zip(fieldList, LOLList):
            plotFieldAllSim(rawData,
                            self.simOutput,
                            AOG,
                            field,
                            LOL,
                            species,
                            self.config.plotSimulationsField_xLabel,
                            self.config.plotSimulationsField_yLabel,
                            self.config.plotSimulationsField_cLabel,
                            self.config.plotSimulationsField_order,
                            self.config.plotSimulationsField_extendDirection,
                            self.config.plotSimulationsField_plotter,
                            self.config.plotSimulationsField_plotterArgs,
                            self.config.plotSimulationsField_extendX,
                            self.config.plotSimulationsField_extendY,
                            self.config.plotSimulationsField_nbrXTicks,
                            self.config.plotSimulationsField_nbrYTicks,
                            self.config.plotSimulationsField_nbrCTicks,
                            self.config.plotSimulationsField_xTicksDecimals,
                            self.config.plotSimulationsField_yTicksDecimals,
                            self.config.plotSimulationsField_cTicksDecimals,
                            self.config.plotSimulationsField_colorBar,
                            cmapName,
                            self.config.plotSimulationsField_timeTextPBar,
                            self.config.extensions,
                            self.config.EPSILON)

#__________________________________________________

