# -*- coding: utf-8 -*-
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import logging
import Settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot,update):  #example of bot and answer of user
    text='Вызван /start'
    logging.info(text)
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}!Ты написал:{}".format(update.message.chat.first_name,update.message.text)
    logging.info('User: %s,Chat_id: %s,Message_text: %s',update.message.chat.username,
    update.message.chat.id,update.message.text)

    print(update.message)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(Settings.API_KEY,request_kwargs=Settings.PROXY)
    logging.info('Бот запускается')
    
    dp = mybot.dispatcher    #dispatcher control what happen in chat
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling() # check new in the telegram
    mybot.idle() #work without control stop (infinity job)




main()  