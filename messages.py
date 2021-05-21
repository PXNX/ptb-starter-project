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
