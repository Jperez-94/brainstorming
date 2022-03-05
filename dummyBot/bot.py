import discord
import server
import apiLol

class Bot(server.ServerCfg):
    def __init__(self):
        self.client = discord.Client()
        self.server = server.ServerCfg()
        self.apiLol = apiLol.ApiLol()
        self.parser_json()

        @self.client.event
        async def on_ready():
            self.update_json()

            send_to = self.client.get_channel(self.get_channel_id('banana-messages'))
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
                    res_message = f'{message.author.name}, ya tenías casa en esta jungla!'
                else:
                    res_message = f'Bienvenido a la jungla {message.author.name}!'
                await message.channel.send(res_message)
            elif message.content.startswith('!addmylol'):
                if message.content.find(' ') == -1:
                    await message.channel.send('Te falta un espacio despues del comando bananita!')
                    return
                self.apiLol.updateSummoner(message)
                await message.channel.send('Uuuuh bananita! Veamos si eres un intrépido guerrero...')
            elif message.author == self.client.user:
                return
            else:
                if message.author.name in self.Members:
                    await message.channel.send('Hola holita bananita!')
                else:
                    await message.channel.send(f'Hola bananita, todavia no nos conocemos. Escribe !newmember para registrarte monete!')