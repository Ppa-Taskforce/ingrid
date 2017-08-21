from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# Say hi when initiating a chat with '/start'
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

# Echo back everything that is not a command
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

if __name__ == "__main__":

    # Get the telegram token
    a = open("apiKey", "r")
    secret = a.readline().rstrip() # Strip the newline!
    a.close()

    # Send the api key to the bot
    updater = Updater(secret)
    dispatcher = updater.dispatcher # Quicker access to the dispatcher used by Updater

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Say hi when initiating a chat with '/start'
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Echo back everything that is not a command
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    # Run it!
    updater.start_polling()
