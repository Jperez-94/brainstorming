import discord

class ServerCfg():
    def __init__(self):
        self._data_json = ""
        self.TextChannels = list()
        self.VoidChannels = list()
        self.Members = list()
    
    def get_Textchannel_id(self, channel_name) -> int:
        if channel_name in self._data_json['TextChannels']:
            return self._data_json['TextChannels'][channel_name]['id']

    def add_Member(self, new_member):
        if new_member[0] in self._data_json['Members']:
            return False
        else:
            self._data_json['Members'][new_member[0]] = {}
            self._data_json['Members'][new_member[0]]["name"] = new_member[0]
            self._data_json['Members'][new_member[0]]["id"] = new_member[1]

    def get_server_TextChannels(self, server_channels):
        for channel in server_channels:
            if type(channel) is discord.channel.TextChannel:
                self._data_json['TextChannels'][channel.name] = {}
                self._data_json['TextChannels'][channel.name]['name'] = channel.name
                self._data_json['TextChannels'][channel.name]['id'] = channel.id
    
    def get_server_VoiceChannels(self, server_channels):
        for channel in server_channels:
            if type(channel) is discord.channel.VoiceChannel:
                self._data_json['VoiceChannels'][channel.name] = {}
                self._data_json['VoiceChannels'][channel.name]['name'] = channel.name
                self._data_json['VoiceChannels'][channel.name]['id'] = channel.id
    
    # Get all members in the server when the Bot has admin permission
    def get_server_Members(self, server_members):
        for server_member in server_members:
            self._data_json['Members'][server_member.name] = {}
            self._data_json['Members'][server_member.name]["name"] = server_member.name
            self._data_json['Members'][server_member.name]["id"] = server_member.id
