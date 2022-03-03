from email import message
import os
import discord
from bot import Bot
from dotenv import load_dotenv

load_dotenv()

# bot = commands.Bot(command_prefix = '!')


bot = Bot()


@bot.client.event
async def on_ready():
    bot.update_json()

    send_to = bot.client.get_channel(bot.get_channel_id('banana-messages'))
    await send_to.send('Hola holita, ya estamos por aquí!')
                
@bot.client.event
async def on_message(message):
    if message.content.startswith('!close'):
        send_to = bot.client.get_channel(bot.get_channel_id('banana-messages'))
        await send_to.send('Se acabó la diversion!')
        await bot.client.close()
    elif message.author == bot.client.user:
        return
    else:
        await message.channel.send('Hola holita bananita!') 
    

bot.client.run(os.getenv('DISCORD_TOKEN'))