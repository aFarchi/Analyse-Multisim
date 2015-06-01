#________________
# preprocessor.py
#________________

from preprocessRawData.rawDataPreprocessor import RawDataPreprocessor

#__________________________________________________

class Preprocessor:

    def __init__(self, config):
        self.rawDataPreprocessor = RawDataPreprocessor(config)

    #_________________________

    def run(self, **kwargs):
        self.rawDataPreprocessor.run(**kwargs)

#__________________________________________________
