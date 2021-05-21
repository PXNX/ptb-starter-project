import logging
import os

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from config import ERROR_GROUP, TOKEN, VERIFIED_USERS, PORT
from messages import *
from utils import remove_message

##########################################
# this file serves as an entry point to the program.
# here all the stuff is initialized.
##########################################


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(ERROR_GROUP,
                             "<b>🤖 Affected Bot</b>\n@" + context.bot.username +
                             "\n\n<b>⚠ Error</b>\n<code>" + str(context.error) +
                             "</code>\n\n<b>Caused by Update</b>\n<code>" + str(update) + "</code>",
                             ParseMode.HTML)


if __name__ == '__main__':
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text(["remove me", "remove me aswell"]), remove_message))

    dp.add_handler(CommandHandler("secret_command", secret_command, Filters.chat(VERIFIED_USERS)))

    dp.add_handler(MessageHandler(Filters.chat_type.private, private_not_available))
    #  add commands below. follow this scheme:  "command", function

    # add commands above this comment

    # comment this one out for full stacktrace
    dp.add_error_handler(error)

    # if using heroku use following instead:
    # updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://YOUR-APP-NAME.herokuapp.com/' + TOKEN)
    updater.start_polling()

    updater.idle()
