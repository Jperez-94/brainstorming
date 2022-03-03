import discord
import server

class Bot(server.ServerCfg):
    def __init__(self):
        self.client = discord.Client()
        self.server = server.ServerCfg()
        self.parser_json()