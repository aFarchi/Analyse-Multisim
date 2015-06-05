#_________________
# fieldsPlotter.py
#_________________

from plotFields.fieldsPlotter import FieldsPlotter 

#__________________________________________________

class SimulationsPlotter:

    def __init__(self, config):
        self.fieldsPlotter = FieldsPlotter(config)

    #_________________________

    def plot(self, **kwargs):
        self.fieldsPlotter.plot(**kwargs)

#__________________________________________________
