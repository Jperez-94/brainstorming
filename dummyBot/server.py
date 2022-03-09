import discord
from macros import json_key

class ServerCfg():
    def __init__(self):
        self._data_json = ""
        self.TextChannels = list()
        self.VoidChannels = list()
        self.Members = list()
    
    def get_Textchannel_id(self, channel_name) -> int:
        if channel_name in self._data_json[json_key.TextChannels]:
            return self._data_json[json_key.TextChannels][channel_name][json_key.Id]

    def add_Member(self, new_member):
        if new_member[0] in self._data_json[json_key.Members]:
            return False
        else:
            self._data_json[json_key.Members][new_member[0]] = {}
            self._data_json[json_key.Members][new_member[0]][json_key.Name] = new_member[0]
            self._data_json[json_key.Members][new_member[0]][json_key.Id] = new_member[1]

    def get_server_TextChannels(self, server_channels) -> None:
        for channel in server_channels:
            if type(channel) is discord.channel.TextChannel:
                self._data_json[json_key.TextChannels][channel.name] = {}
                self._data_json[json_key.TextChannels][channel.name][json_key.Name] = channel.name
                self._data_json[json_key.TextChannels][channel.name][json_key.Id] = channel.id
    
    def get_server_VoiceChannels(self, server_channels) -> None:
        for channel in server_channels:
            if type(channel) is discord.channel.VoiceChannel:
                self._data_json[json_key.VoiceChannels][channel.name] = {}
                self._data_json[json_key.VoiceChannels][channel.name][json_key.Name] = channel.name
                self._data_json[json_key.VoiceChannels][channel.name][json_key.Id] = channel.id
    
    # Get all members in the server when the Bot has admin permission
    def get_server_Members(self, server_members) -> None:
        for server_member in server_members:
            self._data_json[json_key.Members][server_member.name] = {}
            self._data_json[json_key.Members][server_member.name][json_key.Name] = server_member.name
            self._data_json[json_key.Members][server_member.name][json_key.Id] = server_member.id
