import word2art_normalize__wiki_main as p
import level_search as l
import tiktoxt as ti
import telebot
from telebot import types
from telebot import util

token = "1698176432:AAG2dn_P2a64nOzqh-mpj2Rku19hFz_4xQE"
bot = telebot.TeleBot(token, parse_mode=None, threaded=False)
have_level = False
have_text = False

def return_words(text, level):
    link = ti.choose_word(l.hard_words_search(text, level))
    x = l.HardWords(text, level) + '\n' + 'Отдохните от учёбы! Погрузитесь в русский тикток:' + link
    if len(x) > 1:
        return x
    else:
        return 'нет слов...'

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Это бот-помощник изучающим РКИ. Введите текст и ваш уровень владения языком, а бот выведет вам все слова, которые вы можете не знать в этом тексте и тикток по одному из слов. Чтобы начать, нажмите /start.")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте! Давайте начинать! С каким текстом работаем сегодня?")
    global have_level
    global have_text
    have_level = False
    have_text = False

@bot.message_handler(func=lambda message: message.text in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2'))
def getting_level(message):
    cid = message.chat.id
    global level
    global have_level
    global have_text
    level = message.text
    have_level = True
    if have_text == False:
        hideboard=types.ReplyKeyboardRemove()
        bot.reply_to(message, "Теперь введите текст!", reply_markup=hideboard)
    else:
        hideboard=types.ReplyKeyboardRemove()
        bot.reply_to(message, 'Список слов, которые вы можете не знать:', reply_markup=hideboard)
        large_text = return_words(text, level)
        splitted_text = util.split_string(large_text, 3000)
        for message_text in splitted_text:
            bot.send_message(cid, message_text)
        have_text = False
        have_level = False

@bot.message_handler(func=lambda message: True)
def getting_text(message):
    cid = message.chat.id
    global text
    global have_text
    global have_level
    text = message.text
    have_text = True
    if have_level == False:
        markup = types.ReplyKeyboardMarkup()
        itembtna1 = types.KeyboardButton('A1')
        itembtna2 = types.KeyboardButton('A2')
        itembtnb1 = types.KeyboardButton('B1')
        itembtnb2 = types.KeyboardButton('B2')
        itembtnc1 = types.KeyboardButton('C1')
        itembtnc2 = types.KeyboardButton('C2')
        markup.row(itembtna1, itembtna2, itembtnb1)
        markup.row(itembtnb2, itembtnc1, itembtnc2)
        bot.reply_to(message, "Теперь выберите свой уровень:", reply_markup=markup)
    else:
        hideboard=types.ReplyKeyboardRemove()
        bot.reply_to(message, 'Список слов, которые вы можете не знать:', reply_markup=hideboard)
        large_text = return_words(text, level)
        splitted_text = util.split_string(large_text, 3000)
        for message_text in splitted_text:
            bot.send_message(cid, message_text)
        have_text = False
        have_level = False

bot.polling()
