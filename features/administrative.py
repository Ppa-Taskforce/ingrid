from functools import wraps
from features.libraries.mwt import MWT
import os
import time
import sys

# reply to all commands that were not recognized by the previous handlers.
def unknown(bot, update):
    """ Return an error to the user if (s)he uses an invalid command."""
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

# Cached Telegram group administrator check
# If you want to limit certain bot functions to group administrators, you have to test if a user is an administrator in the group in question. This however requires an extra API request, which is why it can make sense to cache this information for a certain time, especially if your bot is very busy.
@MWT(timeout=60*60)
def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]

# Restrict access to a handler (decorator)
# This decorator allows you to restrict the access of a handler to only the user_ids specified in LIST_OF_ADMINS.
# Usage:
# Add a @restricted decorator on top of your handler declaration:

# LIST_OF_ADMINS = [43816335] # Mark, ...
# LIST_OF_ADMINS = get_admin_ids(bot, update.message.chat_id)
global LIST_OF_ADMINS
LIST_OF_ADMINS = [admin.user.id for admin in bot.get_chat_administrators(chat_id)]

def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(bot, update, *args, **kwargs)
    return wrapped

# Example (just add @restricted before the function)
@restricted
def my_handler(bot, update):
    pass  # only accessible if `user_id` is in `LIST_OF_ADMINS`.

def am_admin(bot, update):
    if user_id in LIST_OF_ADMINS:
        bot.send_message(chat_id=update.message.chat_id, text="You are an admin!")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="No admin powers for you!")

@MWT(timeout=60*60)
def my_id(bot, update):
    """Print the user id."""
    user_id = update.effective_user.id
    bot.send_message(chat_id=update.message.chat_id, text="Your user id is: {}.".format(user_id))

@restricted
def restart(bot, update):
    """Restarts the bot."""
    bot.send_message(update.message.chat_id, "Bot is restarting...")
    time.sleep(0.2)
    os.execl(sys.executable, sys.executable, *sys.argv)
