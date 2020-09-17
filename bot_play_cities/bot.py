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

lst = ['Москва', 'Омск', 'Владимир', 'Ашхабад', 'Кострома']

def string_def(user_message):
    print(user_message)
    um=str(user_message)
    spl=um.split()
    ln=len(spl)
    print(ln)
    return ln



def talk_to_me(update, context):


    user_message = update.message.text
    last_letter=user_message[-1].upper()
    # last_letter=update.message.text
    print(last_letter)
    print(user_message)
    update.message.reply_text(user_message)

    if user_message in lst:
        update.message.reply_text(f'Бот: {last_letter}, ваш ход')
        lst.remove(user_message)

        print(lst)
    else:
        update.message.reply_text('Нет города в списке.Начните заново')
        update.message.reply_text(lst)


def play(update, context):
    update.message.reply_text("Введите город")

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("play",play))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
