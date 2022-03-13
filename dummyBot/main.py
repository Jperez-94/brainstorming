from bot import Bot
import threading


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