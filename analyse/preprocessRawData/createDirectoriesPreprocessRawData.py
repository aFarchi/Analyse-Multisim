#______________________________________
# createDirectoriesPreprocessRawData.py
#______________________________________

from itertools                import product

from ..utils.io.write         import createDirectories
from ..utils.analyse.navigate import *

#__________________________________________________

def createDirectoriesPreprocessRawData(simOutput, printIO):
    dirs = []
    for (AOG, lol) in product(AirOrGround(), LinOrLog()):
        for field in simOutput.fieldList[AOG]:
            dirs.append(simOutput.scalingFieldDir(AOG, field, lol))
            for proc in procList:
                dirs.append(simOutput.procPreprocessedFieldDir(proc, AOG, field, lol))

    createDirectories(dirs, printIO)

#__________________________________________________

