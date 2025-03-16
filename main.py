import telebot
from datetime import datetime

# Твой токен бота (замени на актуальный и храни в безопасном месте)
TOKEN = "7861992774:AAGhdUe8N_Kb6e_Ss5EPQYUahI_FV_R99qI"
bot = telebot.TeleBot(TOKEN)

# Дата окончания сезона
TARGET_DATE = datetime(2025, 6, 3)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот помогает определить, сколько побед в день нужно для получения медали 2 сезона премьера в CS2.")
    bot.send_message(message.chat.id, "Введите текущее количество побед в премьер-режиме.")

# Обработчик команды /days_left
@bot.message_handler(commands=['days_left'])
def days_left(message):
    today = datetime.today()
    delta = (TARGET_DATE - today).days
    bot.send_message(message.chat.id, f"До 3 июня 2025 года осталось {delta} дней.")

# Обработчик чисел от пользователя
@bot.message_handler(func=lambda message: message.text.isdigit())
def check_medal_progress(message):
    number = int(message.text)
    remaining_wins = 125 - number
    today = datetime.today()
    remaining_days = (TARGET_DATE - today).days

    if remaining_wins <= 0:
        bot.send_message(message.chat.id, "Ты уже имеешь медаль максимального уровня.")
    else:
        wins_text = "побед" if remaining_wins % 10 in [0, 5, 6, 7, 8, 9] or (10 <= remaining_wins % 100 <= 20) else "победы" if remaining_wins % 10 in [2, 3, 4] else "победа"
        days_text = "дней" if remaining_days % 10 in [0, 5, 6, 7, 8, 9] or (10 <= remaining_days % 100 <= 20) else "дня" if remaining_days % 10 in [2, 3, 4] else "день"
        
        bot.send_message(message.chat.id, f"Тебе осталось {remaining_wins} {wins_text} до 125.")
        
        if remaining_days > 0:
            wins_per_day = remaining_wins / remaining_days
            bot.send_message(message.chat.id, f"Это примерно {wins_per_day:.2f} побед в день.")
        else:
            bot.send_message(message.chat.id, "Времени уже не осталось!")
        
        bot.send_message(message.chat.id, f"До конца сезона осталось {remaining_days} {days_text}.")

# Запуск бота
bot.polling(none_stop=True)
