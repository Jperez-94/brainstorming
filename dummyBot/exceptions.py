from macros import errorMessages as ex

class ConfigurationFail(Exception):
    def __init__(self):
        self.error = ex.ErrorConfig
        super().__init__(self.error)