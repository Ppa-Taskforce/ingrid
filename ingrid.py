import logging
from __future__ import absolute_import

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

from features import social
from features import administrative

# Say hi when initiating a chat with '/start'
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    # formatter = logging.Formatter('%(asctime)s : %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)

def main():
    # Get the telegram token
    a = open("apiKey", "r")
    secret = a.readline().rstrip() # Strip the newline!
    a.close()

    # Send the api key to the bot
    updater = Updater(secret)
    dispatcher = updater.dispatcher # Quicker access to the dispatcher used by Updater

    # Momenteel geen logging naar debug. Ik snap niet waarom...

    # Enable logging
    # Log to different files
    setup_logger('debug', r'ingrid_debug.log')
    setup_logger('info', r'ingrid_info.log')
    setup_logger('warning', r'ingrid_warning.log')
    setup_logger('error', r'ingrid_error.log')
    setup_logger('critical', r'ingrid_critical.log')

    # Set up the different logs
    debug = logging.getLogger('debug')
    info = logging.getLogger('info')
    warning = logging.getLogger('warning')
    error = logging.getLogger('error')
    critical = logging.getLogger('critical')

    # Log some bogus to the log files for testing
    # debug.debug('Initiate logging for debug!')
    # info.info('Initiate logging for info!')
    # warning.warning('Initiate logging for warning!')
    # error.error('Initiate logging for error!')
    # critical.critical('Initiate logging for critical!')

    # Commence zee logging!
    logging.getLogger('debug')
    logging.getLogger('info')
    logging.getLogger('warning')
    logging.getLogger('error')
    logging.getLogger('critical')

    # Say hi when initiating a chat with '/start'
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Echo back everything that is not a command
    # echo_handler = MessageHandler(Filters.text, social.echo)
    # dispatcher.add_handler(echo_handler)

    # Return a message in all CAPS with "/caps <message>"
    # caps_handler = CommandHandler('caps', social.caps, pass_args=True)
    # dispatcher.add_handler(caps_handler)

    # Return a message inline in all CAPS with "@ingridtbot caps <message>"
    # inline_caps_handler = InlineQueryHandler(social.inline_caps)
    # dispatcher.add_handler(inline_caps_handler)

    # Return the user id
    userid_handler = CommandHandler('my_id', administrative.my_id)
    dispatcher.add_handler(userid_handler)

    # Restart the bot (only admins can do that)
    dispatcher.add_handler(CommandHandler('r', administrative.restart))

    # Is the user an admin?
    dispatcher.add_handler(CommandHandler('am_admin', administrative.am_admin))

    # reply to all commands that were not recognized by the previous handlers.
    # Needs to be the last function called!
    unknown_handler = MessageHandler(Filters.command, administrative.unknown)
    dispatcher.add_handler(unknown_handler)

    # Run it!
    updater.start_polling()
    updater.idle() # added for test purposes to disable needless threading.

if '__main__' == __name__:
    main()

# NameError: name 'bot' is not defined
