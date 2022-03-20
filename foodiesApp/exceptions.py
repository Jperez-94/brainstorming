from default import *

class strTypeError(Exception):
    def __init__(self, *args) -> None:
        self.message = ErrorMessage.strTypeError.format(type(args[0]))
        super().__init__(self.message)

class dataBaseKeyNotFound(Exception):
    def __init__(self, *args) -> None:
        self.message = ErrorMessage.dataBaseKeyNotFound.format(args[0])
        super().__init__(self.message)

class frameNotConfigured(Exception):
    def __init__(self) -> None:
        self.message = ErrorMessage.frameNotConfigured
        super().__init__()

class frameWrongFormat(Exception):
    def __init__(self) -> None:
        self.message = ErrorMessage.frameWrongFormat
        super().__init__(self.message)

class emptyDataBase(Exception):
    def __init__(self) -> None:
        self.message = ErrorMessage.emptyDataBase
        super().__init__(self.message)

class newEntryRepeat(Exception):
    def __init__(self, *args) -> None:
        self.message = ErrorMessage.newEntryRepeat.format(args[0])
        super().__init__(*args)

class dataFrameTypeError(Exception):
    def __init__(self, *args) -> None:
        self.message = ErrorMessage.dataFrameTypeError.format(args[0])
        super().__init__(self.message)

class indexEntryNotFound(Exception):
    def __init__(self, *args) -> None:
        self.message = ErrorMessage.indexEntryNotFound.format(args[0])
        super().__init__(self.message)