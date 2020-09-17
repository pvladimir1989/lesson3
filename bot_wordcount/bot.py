from emoji import emojize
from glob import glob
import logging
from random import choice, randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def string_def(user_message):
    print(user_message)
    um=str(user_message)
    spl=um.split()
    ln=len(spl)
    print(ln)
    return ln

def talk_to_me(update, context):

    user_message = update.message.text
    if user_message=="":
        update.message.reply_text("Вы ничего не ввели. Введите текст заново")
        user_message = update.message.text
        count_w = string_def(user_message)
        update.message.reply_text(count_w)
    else:
        count_w=string_def(user_message)
        update.message.reply_text(count_w)


def word_count(update, context):
    update.message.reply_text("Введите текст")

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("wordcount",word_count))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
