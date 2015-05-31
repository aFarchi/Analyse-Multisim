#______________________
# simulationsPlotter.py
#______________________

from plotSimulationsField.simulationsFieldsPlotter import SimulationsFieldPlotter

#__________________________________________________

class SimulationsPlotter:

    def __init__(self, config):
        self.simulationsFieldPlotter = SimulationsFieldPlotter(config)

    #_________________________

    def plot(self, **kwargs):
        self.simulationsFieldPlotter.plot(**kwargs)

#__________________________________________________
