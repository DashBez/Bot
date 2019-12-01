"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import Settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date,datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)



def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Привет {}!Ты написал:{}".format(update.message.chat.first_name,update.message.text)
    logging.info('User: %s,Chat_id: %s,Message_text: %s',update.message.chat.username,
    update.message.chat.id,update.message.text)

    print(update.message)
    update.message.reply_text(user_text)
 

def planet(bot, update):
    #planets = ['Sun','Mercury','Venera','Earth','Mars','Jupyter','Saturn','Uran','Neptun']
    user_text = update.message.text
    planet = user_text.split(' ')[-1].lower()
    now = datetime.now()
    Year = now.strftime("%Y")
    
    if planet == 'mars':
        const = ephem.constellation(ephem.Mars(Year))
        print(const)
    elif planet == 'sun':
        const = ephem.constellation(ephem.Sun(Year))
        print(const)    
    elif planet == 'mercury':
        const = ephem.constellation(ephem.Mercury(Year))
        print(const)    
    elif planet == 'earth':
        const = ephem.constellation(ephem.Earth(Year))
        print(const)          
    elif planet == 'venera':
        const = ephem.constellation(ephem.Venera(Year))
        print(const)     
    elif planet == 'jupyter':
        const = ephem.constellation(ephem.Jupyter(Year))
        print(const)   
    elif planet == 'saturn':
        const = ephem.constellation(ephem.Saturn(Year))
        print(const)  
    elif planet == 'uran':
        const = ephem.constellation(ephem.Uran(Year))
        print(const)       
    elif planet == 'neptun':
        const = ephem.constellation(ephem.Neptun(Year))
        print(const)                       
    
    update.message.reply_text(const)

def main():
    mybot = Updater(Settings.API_KEY,request_kwargs=Settings.PROXY)
    logging.info('Бот запускается')
    
    dp = mybot.dispatcher    #dispatcher control what happen in chat
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling() # check new in the telegram
    mybot.idle() #work without control stop (infinity job)


if __name__ == "__main__":
    main()
