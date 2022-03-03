from http import server
import json

class ServerCfg():
    def __init__(self):
        self.TextChannels = list()
        self.VoidChannels = list()
        self.Members = list()
        self._json_filepath = f'{__file__[0:__file__.find("server.py")]}server_config.json'
        self._data_json = ""
        

    def parser_json(self):
        with open(self.server._json_filepath) as file:
            self._data_json = json.load(file)
        
        self.TextChannels = self._data_json['TextChannels']
        self.VoidChannels = self._data_json['VoiceChannels']
        self.Members = self._data_json['Members']

        file.close()

    def update_json(self):
        self.get_TextChannels_id()
        self.get_VoiceChannels_id()
        self.get_Members_id()

        with open(self.server._json_filepath, 'w') as file:
            json.dump(self._data_json, file, indent= 4)

        file.close()
        self.parser_json()

    

    def get_TextChannels_id(self):
        for server_channel in self.client.get_all_channels():
            # if (server_channel.name in self.TextChannels) is False:
            #     self._data_json['TextChannels'].append({
            #         "channel": {
            #             "name": server_channel.name,
            #             "id": ""
            #         }
            #     }
            #     )
            for json_channel in self._data_json["TextChannels"]:
                self._data_json['TextChannels'][json_channel]['id'] = server_channel.id
    
    def get_VoiceChannels_id(self):
        for server_channel in self.client.get_all_channels():
            # if (server_channel.name in self.TextChannels) is False:
            #     self._data_json['TextChannels'].append({
            #         "channel": {
            #             "name": server_channel.name,
            #             "id": ""
            #         }
            #     }
            #     )
            for json_channel in self._data_json["VoiceChannels"]:
                self._data_json['VoiceChannels'][json_channel]['id'] = server_channel.id
    
    def get_Members_id(self):
        for server_member in self.client.get_all_members():
            # if (server_channel.name in self.TextChannels) is False:
            #     self._data_json['TextChannels'].append({
            #         "channel": {
            #             "name": server_channel.name,
            #             "id": ""
            #         }
            #     }
            #     )
            for json_member in self._data_json["Members"]:
                self._data_json['Members'][json_member]['id'] = server_member.id

    def get_channel_id(self, channel_name):
        return self.TextChannels[channel_name]['id']