# Echo back everything that is not a command
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

# Return a message in all CAPS with "/caps <message>"
def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

# Return a message inline in all CAPS with "@ingridtbot caps <message>"
def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)
