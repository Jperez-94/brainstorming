import discord
import server
import apiLol.apiLol as apiLol
import json
from macros import json_key, commands, admin, messages, tiers
import exceptions as ex
from dotenv import load_dotenv
import os
load_dotenv()

class Bot():

    def __init__(self):
        self.client = discord.Client()
        self.server = server.ServerCfg()
        self.apiLol = apiLol.ApiLol()
        self._killExecution = False
        self.environment = os.getenv('DISCORD_TOKEN')
        self._json_filepath = f'{__file__[0:__file__.find(admin.BOT_FILE)]}{admin.JSON_FILE}'
        self._data_json = ""
        self.parser_json()
    

        @self.client.event
        async def on_ready() -> None:
            self.update_json()
            if self.checkConfiguration():
                await self.client.close()
                raise ex.ConfigurationFail
            if self.checkEmojis():
                await self.client.close()
                raise ex.EmojisFail

            send_to = self.client.get_channel(self.server.get_Textchannel_id(admin.DEFAULT_CHANNEL))
            
            await send_to.send(messages.on_ready)
                        
        @self.client.event
        async def on_message(message) -> None:
            if message.author == self.client.user:
                return

            elif admin.ADMIN not in self._data_json[json_key.Members].keys():
                if message.author.name != admin.ADMIN or self.checkForCommand(message) != commands.NewMember:
                    await message.channel.send(messages.adminRequest.format(admin.ADMIN))
                else:
                    self._set_action(commands.NewMember, message)
                    await message.channel.send(messages.adminRegister.format(message.author.name))

            elif (message.author.name in self.server.Members) is False and self.checkForCommand(message) != commands.NewMember:
                if self.checkForCommand(message) != commands.Close:
                    await message.channel.send(messages.notKnowMember)

            elif self.checkForCommand(message) in commands.Command_List:
                bot_answer = self._set_action(self.checkForCommand(message), message)
                await message.channel.send(bot_answer)
                if self._killExecution:
                    self._killExecution = False
                    await self.client.close()
            
            else:
                await message.channel.send(messages.default)

                
    
    def _set_action(self, command, user_message):
        if command in commands.Restrict_List and user_message.author.name != admin.ADMIN:
            return messages.restricFeature
        
        elif command == commands.Close:
            self._killExecution = True
            return messages.close
        
        elif command == commands.Commands:
            return messages.allCommands
        
        elif command == commands.NewMember:
            new_member = [user_message.author.name, user_message.author.id]
            res = self.server.add_Member(new_member)
            self.update_json()
            if res is False:
                return messages.alreadyRegistered.format(user_message.author.name)
            else:
                return messages.welcomeNewMember.format(user_message.author.name)

        elif command == commands.AddMyLol:
            if user_message.content.find(' ') == -1:
                return messages.badCommandFormat

            self.parser_json()
            res = self.apiLol.updateSummoner(user_message)
            self._data_json = self.apiLol._data_json
            self.update_json()
            if res:
                bot_message = messages.checkSummonerDefault
                res = self.apiLol.updateSummonerInfo(user_message.author.name)
                self._data_json = self.apiLol._data_json
                self.update_json()
                if res:
                    bot_message += messages.summonerFound.format(
                        self._data_json[json_key.Members][user_message.author.name][json_key.Summoner][json_key.Tier],
                        self._data_json[json_key.Members][user_message.author.name][json_key.Summoner][json_key.Division]
                    )
                else:
                    bot_message += messages.summonerNotRanked
                
                return bot_message

            else:
                return messages.summonerNotFound

        elif command ==commands.Rank:
            self.parser_json()
            res = self.apiLol.rankMembers()
            self._data_json = self.apiLol._data_json
            self.update_json()
            
            if len(res) != 0:
                answer = messages.introRank
                for el in res:
                    answer += messages.rankMessage.format(self.apiLol.Icons[el[0]], el[1], el[2], el[3])
                
                return answer
            else:
                return messages.rankUnable
        
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

    def checkConfiguration(self) -> bool:
        if admin.REGION == "":
            return True
        elif admin.APILOLKEY == "":
            return True
        elif admin.ADMIN == "":
            return True
        elif admin.DEFAULT_CHANNEL == "" or admin.DEFAULT_CHANNEL not in self._data_json[json_key.TextChannels].keys():
            return True
        else:
            return False

    def checkEmojis(self) -> bool:
        emojisList = self.client.emojis
        for emoji in emojisList:
            if emoji.name not in tiers.Tier_List:
                return True
        
        return False