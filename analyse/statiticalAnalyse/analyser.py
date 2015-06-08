#____________
# analyser.py
#____________

from performStatisticalAnalyse.statisticalAnalyser import StatisticalAnalyser

#__________________________________________________

class Analyser:

    def __init__(self, config):
        self.statisticalAnalyser = StatisticalAnalyser(config)

    #_________________________

    def run(self, **kwargs):
        self.statisticalAnalyser.run(**kwargs)

#__________________________________________________
