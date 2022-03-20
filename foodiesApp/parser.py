import exceptions as ex
import json

class DataBase():
    def __init__(self) -> None:
        self._dataBaseFile = f'{__file__[0:__file__.find("parser.py")]}{"database.json"}'

    def getKeybyNumber(self, index) -> None:
        if type(index) != str:
            raise ex.strTypeError(index)
        
        dataBase = self._readDataBase()

        if index not in dataBase.keys():
            raise ex.dataBaseKeyNotFound(index)
        
        return dataBase[index]
        
    def _readDataBase(self) -> dict:
        dataBase = dict()
        with open(self._dataBaseFile) as file:
            dataBase = json.load(file)
        
        file.close()
        return dataBase
    
    def _writeDataBase(self, dataBase) -> None:
        with open(self._dataBaseFile, 'w') as file:
            json.dump(dataBase, file, indent= 4)


class DataFrame():
    def __init__(self, *args) -> None:
        self.frame = args[0]
        self.name = str
        self.direction = str
        self.type = str
        self._parserFrame()
    
    def _parserFrame(self) -> None:
        if type(self.frame) != dict:
            raise ex.frameNotConfigured
        if 'name' not in self.frame.keys() or 'direction' not in self.frame.keys() or 'type' not in self.frame.keys():
            raise ex.frameWrongFormat

        self.name = self.frame["name"]
        self.direction = self.frame["direction"]
        self.type = self.frame["type"]

