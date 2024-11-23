#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging, json

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, WebAppInfo
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# GENDER, PHOTO, LOCATION, BIO = range(4)
LOGIN, CENTRE, CATEGORY, SUB_CATEGORY, SLOT, FORM, DATE = range(7)
reply_keyboard = [["Success", "Fail"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""

    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Please send me login information",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return LOGIN


async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    keyword = update.message.text
    if keyword == "Success":
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Login Successfully, please choose your centre on the list below",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return CENTRE
    else:
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Login Unsuccessfully, please send login info again",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return LOGIN


async def back_login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Came back, please send login info again",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return LOGIN


async def centre(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    keyword = update.message.text
    if keyword == "Success":
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Gorgeous! Now, select your category please",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return CATEGORY
    else:
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "There is no category available for this centre, please choose other centre",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return CENTRE


async def back_centre(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Came back, please choose your centre again",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return CENTRE


async def category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    keyword = update.message.text
    if keyword == "Success":
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Gorgeous! Now, select your sub-category please",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return SUB_CATEGORY
    else:
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "There is no sub-category available for this category, please choose other category",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return CATEGORY


async def back_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Came back, please choose your category again",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return CATEGORY


async def sub_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    keyword = update.message.text
    if keyword == "Success":
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Gorgeous! Now, select your slot please",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return SLOT
    else:
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "There is no slot available, please choose other sub-category",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return SUB_CATEGORY


async def back_sub_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Came back, please choose your sub-category again",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return SUB_CATEGORY


async def slot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    keyword = update.message.text
    if keyword == "Success":
        reply_keyboard = [["Form1", "Form2"]]
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Gorgeous! Now, fill the application in form below please",
            reply_markup=ReplyKeyboardMarkup.from_button(
                KeyboardButton(
                    text="Open the application form!",
                    web_app=WebAppInfo(url="https://hoang97.github.io/vfs-bot"),
                )
            ),
        )
        return FORM
    else:
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Sorry, the slot you chose has been taken, please choose other slot",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return SLOT


async def back_slot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Came back, please choose your slot again",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return SLOT


async def form(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    data = json.loads(update.effective_message.web_app_data.data)
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        f"Form Data: {data}\n\n"
        "Gorgeous, please choose your meeting date",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return DATE


async def back_form(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
        "Send /back to comback to previous step.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Came back, please refill your form again",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
        ),
    )

    return FORM


async def date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    keyword = update.message.text
    if keyword == "Success":
        await update.message.reply_text(
            "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    else:
        await update.message.reply_text(
            "Hi! My name is Professor Bot. I will hold a conversation with you.\n"
            "Send /back to comback to previous step.\n\n"
            "Send /cancel to stop talking to me.\n\n"
            "Sorry, your date is not on the list, please choose another date",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Success or Fail?"
            ),
        )
        return DATE


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7758792964:AAHIvZ9t1jEv4ZKJK6PaXPOIUKZzfVFZWsw").build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    # LOGIN, CENTRE, CATEGORY, SUB_CATEGORY, SLOT, FORM, DATE = range(7)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LOGIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, login)],
            CENTRE: [MessageHandler(filters.TEXT & ~filters.COMMAND, centre), CommandHandler("back", back_login)],
            CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, category), CommandHandler("back", back_centre)],
            SUB_CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, sub_category), CommandHandler("back", back_category)],
            SLOT: [MessageHandler(filters.TEXT & ~filters.COMMAND, slot), CommandHandler("back", back_sub_category)],
            FORM: [MessageHandler(filters.StatusUpdate.WEB_APP_DATA, form), CommandHandler("back", back_slot)],
            DATE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, date),
                CommandHandler("back", back_form),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()