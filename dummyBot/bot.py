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
        self._killExecution = False
        self._json_filepath = f'{__file__[0:__file__.find("bot.py")]}server_config.json'
        self._data_json = ""
        self.parser_json()

        @self.client.event
        async def on_ready() -> None:
            self.update_json()
            self.apiLol.Icons = self.client.emojis
            
            send_to = self.client.get_channel(self.server.get_Textchannel_id('test-channel'))
            await send_to.send('Hola holita, ya estamos por aquí!')
                        
        @self.client.event
        async def on_message(message) -> None:
            if (message.author.name in self.server.Members) is False and self.checkForCommand(message) != commands.NewMember:
                if self.checkForCommand(message) != commands.Close:
                    await message.channel.send(f'Hola bananita, todavia no nos conocemos. Escribe !newmember para registrarte monete!')
            
            elif message.author == self.client.user:
                return

            elif self.checkForCommand(message) in commands.Command_List:
                print(self.checkForCommand(message))
                bot_answer = self.set_action(self.checkForCommand(message), message)
                await message.channel.send(bot_answer)
                if self._killExecution:
                    await self.client.close()
            
            else:
                await message.channel.send('Hola holita bananita!')

                
    
    def set_action(self, command, user_message):
        if command == commands.Close and user_message.author.name == json_key.Admin:
            self._killExecution = True
            return 'Se acabó la diversion!'

        elif command == commands.Close and user_message.author.name != json_key.Admin:
            return 'Bananita! Parece que no sabes que botón tienes que pulsar'
        
        elif command == commands.NewMember:
            new_member = [user_message.author.name, user_message.author.id]
            res = self.server.add_Member(new_member)
            self.update_json()
            if res is False:
                return f'{user_message.author.name}, ya tenías casa en esta jungla! Ya puedes usar las funcionalidades de League of Legends, lo primero es registrar tu nombre de invocador. Escribe !addmylol [nombreInvocador]'
            else:
                return f'Bienvenido a la jungla {user_message.author.name}! Si quieres acceder a las funcionalidades de League of Leagends, añade tu nombre de invocador escribiendo !addmylol [nombreInvocador]'

        elif command == commands.AddMyLol:
            if user_message.content.find(' ') == -1:
                return'Te falta un espacio despues del comando bananita!'

            self.parser_json()
            res = self.apiLol.updateSummoner(user_message)
            self.update_json()
            if res:
                bot_message = 'Uuuuh bananita! Veamos si eres un intrépido invocador...\n'
                res = self.apiLol.updateSummonerInfo(user_message.author.name)
                self.update_json()
                if res:
                    bot_message += f'\nInteresante bananita, estás en {self._data_json[json_key.Members][user_message.author.name][json_key.Summoner][json_key.Tier]} {self._data_json[json_key.Members][user_message.author.name][json_key.Summoner][json_key.Division]}'
                else:
                    bot_message += '\nOh oh bananita! Parece que aun no tienes clasificación'
                
                return bot_message

            else:
                return 'Algo ha salido mal bananita! Revisa que has escrito bien tu nombre de invocador'

        elif command ==commands.Rank:
            self.parser_json()
            res = self.apiLol.rankMembers()
            
            if len(res) != 0:
                answer = "Veamos como va el ranking bananita:\n"
                for el in res:
                    answer += f"            {self.apiLol.Icons[el[0]]} {el[1]} está en {el[2]} {el[3]}\n"
                
                return answer
            else:
                return 'Vaya bananita! No hay ningún invocador registrado o con rango conseguido'
        
        elif command == commands.MyLol:
            mess = self.apiLol.get_summoner_stadistics(user_message.author.name)
            return mess
    
    def parser_json(self) -> None:
        with open(self._json_filepath) as file:
            self._data_json = json.load(file)
            self.server._data_json = self._data_json
            self.apiLol._data_json = self._data_json
        
        self.server.TextChannels = self._data_json[json_key.TextChannels]
        self.server.VoidChannels = self._data_json[json_key.VoiceChannels]
        self.server.Members = self._data_json[json_key.Members]

        file.close()

    def update_json(self) -> None:
        server_channels = self.get_all_channels()
        server_members = self.client.get_all_members()
        self.server.get_server_TextChannels(server_channels)
        self.server.get_server_VoiceChannels(server_channels)
        self.server.get_server_Members(server_members)

        with open(self._json_filepath, 'w') as file:
            json.dump(self._data_json, file, indent= 4)

        file.close()
        self.parser_json()

    def checkForCommand(self, user_message) -> str:
        for command in commands.Command_List:
            if user_message.content.find(command) == 0:
                return command
        
        return None

    def get_all_channels(self) -> list:
        channels = []
        for guild in self.client.guilds:
            for channel in guild.channels:
                channels.append(channel)
        
        return channels
