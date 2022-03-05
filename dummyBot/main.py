import os
from bot import Bot
from dotenv import load_dotenv

load_dotenv()

# bot = commands.Bot(command_prefix = '!')


bot = Bot()

bot.client.run(os.getenv('DISCORD_TOKEN'))