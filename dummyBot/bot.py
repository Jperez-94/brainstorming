import discord
import server
import apiLol.apiLol as apiLol

class Bot(server.ServerCfg):
    def __init__(self):
        self.client = discord.Client()
        self.server = server.ServerCfg()
        self.apiLol = apiLol.ApiLol()
        self.parser_json()

        @self.client.event
        async def on_ready():
            self.update_json()
            
            send_to = self.client.get_channel(self.get_Textchannel_id('banana-messages'))
            await send_to.send('Hola holita, ya estamos por aquí!')
                        
        @self.client.event
        async def on_message(message):
            if message.content.startswith('!close'):
                await message.channel.send('Se acabó la diversion!')
                await self.client.close()

            elif message.content.startswith('!newmember'):
                new_member = [message.author.name, message.author.id]
                res = self.add_Member(new_member)
                if res is False:
                    res_message = f'{message.author.name}, ya tenías casa en esta jungla! Ya puedes usar las funcionalidades de League of Legends, lo primero es registrar tu nombre de invocador. Escribe !addmylol [nombreInvocador]'
                else:
                    res_message = f'Bienvenido a la jungla {message.author.name}! Si quieres acceder a las funcionalidades de League of Leagends, añade tu nombre de invocador escribiendo !addmylol [nombreInvocador]'
                await message.channel.send(res_message)

            elif message.content.startswith('!addmylol'):
                if message.content.find(' ') == -1:
                    await message.channel.send('Te falta un espacio despues del comando bananita!')
                    return
                res = self.apiLol.updateSummoner(message)
                if res:
                    await message.channel.send('Uuuuh bananita! Veamos si eres un intrépido invocador...')
                    res = self.apiLol.updateSummonerInfo(message.author.name)
                    if res:
                        self.update_json()
                        await message.channel.send(f'Interesante bananita, estás en {self._data_json["Members"][message.author.name]["summoner"]["tier"]} {self._data_json["Members"][message.author.name]["summoner"]["division"]}')
                    else:
                        await message.channel.send('Oh oh bananita! Parece que aun no tienes clasificación')
                else:
                    await message.channel.send('Algo ha salido mal bananita! Revisa que has escrito bien tu nombre de invocador')

            elif message.content.startswith('!rank'):
                res = self.apiLol.rankMembers()
                if len(res) != 0:
                    answer = "Veamos como va el ranking bananita:\n"
                    for el in self.apiLol.rankMembers():
                        answer += f"-> {el[0]} está en {el[1]} {el[2]}\n"
                    
                    await message.channel.send(answer)
                else:
                    await message.channel.send('Vaya bananita! No hay ningún invocador registrado o con rango conseguido')

            elif message.author == self.client.user:
                return

            else:
                if message.author.name in self.Members:
                    await message.channel.send('Hola holita bananita!')
                else:
                    await message.channel.send(f'Hola bananita, todavia no nos conocemos. Escribe !newmember para registrarte monete!')