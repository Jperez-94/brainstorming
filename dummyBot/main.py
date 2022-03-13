from bot import Bot
import threading
import time
import os
import sys

# Añadir control de errores
# Añadir servicio de mensajeria enviando reporte con error al admin
# Reset mediante comando
# Añadir reset, desde discord.py no parece posible. Hay que bajar a la capa HTTPS o buscar otra opcion

def createBotInstance():
    return Bot()

def logInBot(bot):
    bot.client.run(bot.environment)


def main():
    bot = createBotInstance()
    thread = threading.Thread(target= logInBot, args= (bot,))
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()