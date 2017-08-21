class Social:

    """
    Implementeer aparte classes voor verschillende features.
    """

    # Echo back everything that is not a command
    def echo(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
