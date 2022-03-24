from parserFoody import *
import random

class Foody():
    def __init__(self) -> None:
        self.DataBase = DataBase()

    def getRandomFoody(self) -> DataFrame:
        numOfFoody = self.DataBase.getNumberOfEntryes()
        random.seed(1)

        return DataFrame(self.DataBase.getEntrybyKey(str(random.randint(0,numOfFoody - 1))))

    def saveNewFoody(self, dataFrame) -> None:
        if type(dataFrame) != DataFrame:
            raise ex.dataFrameTypeError(type(dataFrame))

        self.DataBase.setNewEntry(dataFrame)

    def removeFoody(self, index) -> None:
        self.DataBase.removeEntry(index)
