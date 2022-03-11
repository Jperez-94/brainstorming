import os
from bot import Bot
from dotenv import load_dotenv

load_dotenv()

# Añadir un check de que se tiene la configuracion lista
# Añadir control de errores
# Añadir servicio de mensajeria enviando reporte con error al admin

bot = Bot()

bot.client.run(os.getenv('DISCORD_TOKEN'))