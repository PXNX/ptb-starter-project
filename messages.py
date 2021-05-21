from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from utils import delay_group, delay_group_button_url, now, delay_group_preview


##########################################
# this file contains the actions that will happen once a command is called
# just replicate below schemes :)
##########################################

def secret_command(update: Update, context: CallbackContext):
    update.message.reply_text("Hey! Seems like you're verified.")
    context.bot.send_message(update.message.chat_id, "The secret ingredient is love <3")


def private_not_available(update: Update, context: CallbackContext):
    update.message.reply_text("Heeeey! Stop!"
                              "\n\n<b>This is not something I'm looking for.</b>"
                              "\n\nPlease dn't ask me personal stuff, dude.",
                              parse_mode=ParseMode.HTML)
