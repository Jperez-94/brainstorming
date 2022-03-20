from parserFoody import *
import random

def getRandomFoody() -> DataFrame:
    database = DataBase()
    numOfFoody = database.getNumberOfEntryes()
    random.seed(1)

    return DataFrame(database.getEntrybyKey(str(random.randint(0,numOfFoody - 1))))

def saveNewFoody(dataFrame) -> None:
    dataBase = DataBase()
    if type(dataFrame) != DataFrame:
        raise ex.dataFrameTypeError(type(dataFrame))

    dataBase.setNewEntry(dataFrame)

def removeFoody(index) -> None:
    dataBase = DataBase()
    dataBase.removeEntry(index)

