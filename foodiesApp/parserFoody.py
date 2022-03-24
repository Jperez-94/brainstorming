from default import *
import exceptions as ex
import json

class DataBase():
    def __init__(self) -> None:
        self._dataBaseFile = f'{__file__[0:__file__.find("parserFoody.py")]}{"database.json"}'
    
    def getNumberOfEntryes(self) -> int:
        database = self._readDataBase()
        if len(database.keys()) == 0:
            raise ex.emptyDataBase

        return len(database.keys())

    def getEntrybyKey(self, index) -> None:
        if type(index) != str:
            raise ex.strTypeError(index)
        
        dataBase = self._readDataBase()

        if index not in dataBase.keys():
            raise ex.dataBaseKeyNotFound(index)
        
        return dataBase[index]
    
    def setNewEntry(self, dataFrame) -> None:
        dataBase = self._readDataBase()
        if self._checkNewEntry(dataBase, dataFrame) is False:
            raise ex.newEntryRepeat(dataFrame.name)

        lastEntryKey = len(dataBase.keys()) - 1

        dataBase[str(lastEntryKey + 1)] = {}
        dataBase[str(lastEntryKey + 1)][DataBaseKey.name] = dataFrame.name
        dataBase[str(lastEntryKey + 1)][DataBaseKey.direction] = dataFrame.direction
        dataBase[str(lastEntryKey + 1)][DataBaseKey.foodtype] = dataFrame.foodtype

        self._writeDataBase(dataBase)
    
    def removeEntry(self, index) -> None:
        if type(index) != str:
            raise ex.strTypeError(index)
        
        dataBase = self._readDataBase()
        
        if self._checkIndexEntry(dataBase, index) is False:
            raise ex.indexEntryNotFound(index)

        del dataBase[index]

        self._writeDataBase(dataBase)
    
    def _checkNewEntry(self, dataBase, dataFrame) -> bool:
        for entry in dataBase.keys():
            if dataFrame.name == dataBase[entry][DataBaseKey.name]:
                return False
            if dataFrame.direction == dataBase[entry][DataBaseKey.direction]:
                return False
            if dataFrame.foodtype == dataBase[entry][DataBaseKey.foodtype]:
                return False
        
        return True
    
    def _checkIndexEntry(self, dataBase, index) -> bool:
        for entry in dataBase.keys():
            if entry == index:
                return True
        
        return False
            
    def _readDataBase(self) -> dict:
        dataBase = dict()
        with open(self._dataBaseFile) as file:
            dataBase = json.load(file)
        
        file.close()
        return dataBase
    
    def _writeDataBase(self, dataBase) -> None:
        with open(self._dataBaseFile, 'w') as file:
            json.dump(dataBase, file, indent= 4)
        
        file.close


class DataFrame():
    def __init__(self, *args) -> None:
        self.frame = args[0]
        self.name = str
        self.direction = str
        self.foodtype = str
        self._parserFrame()
    
    def _parserFrame(self) -> None:
        if type(self.frame) != dict:
            raise ex.frameNotConfigured
        if self._checkFrameFormat is False:
            raise ex.frameWrongFormat

        self.name = self.frame[DataBaseKey.name]
        self.direction = self.frame[DataBaseKey.direction]
        self.foodtype = self.frame[DataBaseKey.foodtype]
    
    def _checkFrameFormat(self) -> bool:
        if DataBaseKey.name not in self.frame.keys():
            return False
        if DataBaseKey.direction not in self.frame.keys():
            return False
        if DataBaseKey.foodtype not in self.frame.keys():
            return False
        
        return True