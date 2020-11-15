import os
import telebot
from flask import Flask, request
from rate_processing import RateProcessing as RPClass
from exchange_bot import ExchangeBot as EBClass

rpclass = RPClass(300)
ebclass = EBClass(rpclass)

# server = Flask(__name__)
#
#
# @server.route('/' + ebclass.tg_token, methods=['POST'])
# def getMessage():
#     ebclass.bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
#
#
# @server.route('/')
# def webhook():
#     ebclass.bot.remove_webhook()
#     ebclass.bot.set_webhook(url='https://protected-oasis-53938.herokuapp.com/' + ebclass.tg_token)
#     return '!', 200


def main():
    rpclass.execute()
    ebclass.execute()


if __name__ == '__main__':
    # server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    main()
