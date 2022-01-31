import telebot
import time
import hashlib
from urllib.request import urlopen, Request

bot = telebot.TeleBot("5194896265:AAFAOfT7VjKkbkM_aMs4ik7Ylsb9vzF2WFQ", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "I'm ready!")

#Выбор сайта, за которым надо следить
url = Request('https://habr.com/ru/all/', 
              headers={'User-Agent': 'Mozilla/5.0'})
  
# to perform a GET request and load the 
# content of the website and store it in a var
response = urlopen(url).read()
  
# копирует изначальный хэш сайта
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()
          
        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()
          
        # таймер 30 секунд
        time.sleep(30)
          
        # perform the get request
        response = urlopen(url).read()
          
        # новый хэш
        newHash = hashlib.sha224(response).hexdigest()
  
        # есть новый хэш равен старому, то работает дальше
        if newHash == currentHash:
            continue
  
        # если есть отличия в хэше:
        else:
            # бот пишет письмо
            bot.send_message (369526576, "Есть изменения на сайте")
  
            # again read the website
            response = urlopen(url).read()
  
            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()
  
            # снова ждет 30 секунд
            time.sleep(30)
            continue
              
    # что то связанное с падениями/ошибками
    except Exception as e:
        bot.send_message (369526576, "error")
		