from emoji import emojize
from glob import glob
import logging
from random import choice, randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def minus(a,b):
    return int(a)-int(b)
def plus(a,b):
    return int(a) + int(b)
def mult(a,b):
    return int(a) * int(b)
def div(a,b):
    return int(a) / int(b)

def talk_to_me(update, context):

    user_message = update.message.text
    user_message=str(user_message)

    print(user_message)
    if "-" in user_message:
        spl=user_message.split("-")
        print(spl)
        res=minus(spl[0],spl[1])
        print(res)
        update.message.reply_text(res)
    elif "+" in user_message:
        spl=user_message.split("+")
        print(spl)
        res=plus(spl[0],spl[1])
        print(res)
        update.message.reply_text(res)
    elif "*" in user_message:
        spl = user_message.split("*")
        print(spl)
        res = mult(spl[0], spl[1])
        print(res)
        update.message.reply_text(res)
    elif "/" in user_message:
        spl = user_message.split("/")
        print(spl)
        res = div(spl[0], spl[1])
        print(res)
        update.message.reply_text(res)


def calc(update, context):
    update.message.reply_text("Введите выражение")

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("calc",calc))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
