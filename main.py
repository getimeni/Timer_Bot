import telebot
import time
from telebot.types import Message
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
flag = 'sec'
@bot.message_handler(['start'])
def start(msg: Message):
    kb = telebot.types.ReplyKeyboardMarkup(True,True)
    kb.row('min','sec')
    bot.send_message(msg.chat.id, 'Hello im Bot Timer, choose minutes or seconds',reply_markup=kb)
    bot.register_next_step_handler(msg, quest)

def quest(msg: Message):
    global flag
    if msg.text == 'min':
        flag = 'min'
        bot.send_message(msg.chat.id, 'In how many minutes do i text you?')
    elif msg.text == 'sec':
        bot.send_message(msg.chat.id, 'In how many seconds do i text you?')
    bot.register_next_step_handler(msg, number_check)

def number_check(msg: Message):
    if msg.text.isnumeric():
        if flag == 'min':
            msg.text = int(msg.text)*60
        time.sleep(int(msg.text))
        timer_end(msg, int(msg.text))
    else:
        bot.send_message(msg.chat.id, 'YOU DIDNT USE A NUMBER!')
        quest(msg)

def timer_end(msg: Message, sec: int):
    bot.send_message(msg.chat.id, 'Dzing Dzing!')


bot.infinity_polling()