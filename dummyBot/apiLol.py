import json

class ApiLol():

    def __init__(self):
        self._json_filepath = f'{__file__[0:__file__.find("apiLol.py")]}server_config.json'
        self._data_json = ""
        self.parser_json()
    
    def parser_json(self):
        with open(self._json_filepath) as file:
            self._data_json = json.load(file)

        file.close()

    def update_json(self):
        with open(self._json_filepath, 'w') as file:
            json.dump(self._data_json, file, indent= 4)

        file.close()
        self.parser_json()

    def updateSummoner(self, message):
        discord_member = message.author.name
        summoner = message.content[len('!addmylol') + 1:len(message.content)]
        self._data_json['Members'][discord_member]['summoner'] = summoner
        self.update_json()