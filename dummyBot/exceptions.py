from macros import errorMessages as ex

class ConfigurationFail(Exception):
    def __init__(self) -> None:
        self.error = ex.ErrorConfig
        super().__init__(self.error)

class EmojisFail(Exception):
    def __init__(self) -> None:
        self.error = ex.ErrorEmojis
        super().__init__(self.error)