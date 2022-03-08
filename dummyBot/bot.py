import discord
import server
import apiLol.apiLol as apiLol
import json
from macros import json_key, commands

class Bot():
    def __init__(self):
        self.client = discord.Client()
        self.server = server.ServerCfg()
        self.apiLol = apiLol.ApiLol()
        self._json_filepath = f'{__file__[0:__file__.find("bot.py")]}server_config.json'
        self._data_json = ""
        self.parser_json()

        @self.client.event
        async def on_ready():
            self.update_json()
            self.apiLol.Icons = self.client.emojis
            print(self.apiLol.Icons)
            
            send_to = self.client.get_channel(self.server.get_Textchannel_id('test-channel'))
            await send_to.send('Hola holita, ya estamos por aquí!')
                        
        @self.client.event
        async def on_message(message):
            if message.content.startswith(commands.Close):
                await message.channel.send('Se acabó la diversion!')
                await self.client.close()
            
            elif message.content.startswith(commands.NewMember):
                new_member = [message.author.name, message.author.id]
                res = self.server.add_Member(new_member)
                self.update_json()
                if res is False:
                    res_message = f'{message.author.name}, ya tenías casa en esta jungla! Ya puedes usar las funcionalidades de League of Legends, lo primero es registrar tu nombre de invocador. Escribe !addmylol [nombreInvocador]'
                else:
                    res_message = f'Bienvenido a la jungla {message.author.name}! Si quieres acceder a las funcionalidades de League of Leagends, añade tu nombre de invocador escribiendo !addmylol [nombreInvocador]'
                await message.channel.send(res_message)
            
            elif (message.author.name in self.server.Members) is False:
                await message.channel.send(f'Hola bananita, todavia no nos conocemos. Escribe !newmember para registrarte monete!')

            elif message.content.startswith(commands.AddMyLol):
                if message.content.find(' ') == -1:
                    await message.channel.send('Te falta un espacio despues del comando bananita!')
                    return

                self.parser_json()
                res = self.apiLol.updateSummoner(message)
                self.update_json()
                if res:
                    await message.channel.send('Uuuuh bananita! Veamos si eres un intrépido invocador...')
                    res = self.apiLol.updateSummonerInfo(message.author.name)
                    self.update_json()
                    if res:
                        await message.channel.send(f'Interesante bananita, estás en {self._data_json[json_key.Members][message.author.name][json_key.Summoner][json_key.Tier]} {self._data_json[json_key.Members][message.author.name][json_key.Summoner][json_key.Division]}')
                    else:
                        await message.channel.send('Oh oh bananita! Parece que aun no tienes clasificación')
                else:
                    await message.channel.send('Algo ha salido mal bananita! Revisa que has escrito bien tu nombre de invocador')

            elif message.content.startswith(commands.Rank):
                self.parser_json()
                res = self.apiLol.rankMembers()
                if len(res) != 0:
                    answer = "Veamos como va el ranking bananita:\n"
                    for el in res:
                        answer += f"            {self.apiLol.Icons[el[0]]} {el[1]} está en {el[2]} {el[3]}\n"
                    
                    await message.channel.send(answer)
                else:
                    await message.channel.send('Vaya bananita! No hay ningún invocador registrado o con rango conseguido')

            elif message.author == self.client.user:
                return

            else:
                await message.channel.send('Hola holita bananita!')
    
    def parser_json(self):
        with open(self._json_filepath) as file:
            self._data_json = json.load(file)
            self.server._data_json = self._data_json
            self.apiLol._data_json = self._data_json
        
        self.server.TextChannels = self._data_json[json_key.TextChannels]
        self.server.VoidChannels = self._data_json[json_key.VoiceChannels]
        self.server.Members = self._data_json[json_key.Members]

        file.close()

    def update_json(self):
        server_channels = self.get_all_channels()
        server_members = self.client.get_all_members()
        self.server.get_server_TextChannels(server_channels)
        self.server.get_server_VoiceChannels(server_channels)
        self.server.get_server_Members(server_members)

        with open(self._json_filepath, 'w') as file:
            json.dump(self._data_json, file, indent= 4)

        file.close()
        self.parser_json()

    def get_all_channels(self) -> list:
        channels = []
        for guild in self.client.guilds:
            for channel in guild.channels:
                channels.append(channel)
        
        return channels
