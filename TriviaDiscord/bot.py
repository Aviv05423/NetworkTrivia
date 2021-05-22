import telebot


API_KEY = "1893608043:AAGYZMlDfPfCOIAvZuc3_XLK9D7VDag38eM"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['login'])
def login(message):
    bot.reply_to(message, "hey")

@bot.message_handler(commands=['hi'])
def hi(message):
    bot.send_message(message.chat.id, "hey")


bot.polling()