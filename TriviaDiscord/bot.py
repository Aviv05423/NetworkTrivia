import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardRemove

API_KEY = "1893608043:AAGYZMlDfPfCOIAvZuc3_XLK9D7VDag38eM"
chat_id = ""
bot = telebot.TeleBot(API_KEY)

poll_markup=ReplyKeyboardMarkup(one_time_keyboard=True)
poll_markup.add(KeyboardButton('send me a poll',
                request_poll=KeyboardButtonPollType(type='quiz')))


@bot.message_handler(commands=['login'])
def login(message):
    chat_id = message.chat.id
    bot.reply_to(message, "hey")
    remove_board = ReplyKeyboardRemove()
    bot.send_message(chat_id, "text", reply_markup=poll_markup)




@bot.message_handler(commands=['hi'])
def hi(message):
    bot.send_message(message.chat.id, "hey2")


bot.polling()