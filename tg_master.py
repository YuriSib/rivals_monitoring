import telebot


bot = telebot.TeleBot('6583598966:AAFiH4kjnxOi3PWnmoM5sswFDhPxsejHkrY')


@bot.message_handler(commands=['start'])
def test(message_):
    chat_id = message_.chat.id
    bot.reply_to(message_, f"Your chat ID is: {chat_id}")


def check_message():
    # bot.send_message(-1002049731505, f'Проверка')
    bot.send_message(-2056827090, f'Проверка')


def send_message(key, event):
    text, link = event[0], event[1]
    bot.send_message(-2056827090, f'{key}\n {text}\n{link}')


def error_message(site_name, error_name):
    bot.send_message(674796107, f'При парсинге {site_name} произошла ошибка: \n {error_name}')

