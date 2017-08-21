# Echo back everything that is not a command
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
