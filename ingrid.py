from python-telegram-bot/telegram.ext import Updater
import python-telegram-bot/logging


if __name__ == "__main__":

    # Get the telegram token
    a = open("TOKEN", "r")
    TOKEN = a.read()
    a.close()

    updater = Updater(token='TOKEN')
    dispatcher = updater.dispatcher # Quicker access to the dispatcher used by Updater

