#_________________
# fieldsPlotter.py
#_________________

from plotFields.fieldsPlotter                               import FieldsPlotter as FieldsOnlyPlotter
from plotFieldsAttachGrayScale.fieldsAttachGrayScalePlotter import FieldsAttachGrayScalePlotter

#__________________________________________________

class FieldsPlotter:

    def __init__(self, config):
        self.fieldsPlotter         = FieldsOnlyPlotter(config)
        self.fieldsAttachGSPlotter = FieldsAttachGrayScalePlotter(config)

    #_________________________

    def plot(self, **kwargs):
        self.fieldsPlotter.plot(**kwargs)
        self.fieldsAttachGSPlotter.plot(**kwargs)

#__________________________________________________
