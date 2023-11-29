import telebot


bot = telebot.TeleBot('6419841809:AAFEiToc-LKefUbh7nkzEiusYGnHgA0NAK8')


@bot.message_handler(commands=['start'])
def test(message_):
    chat_id = message_.chat.id
    bot.reply_to(message_, f"Your chat ID is: {chat_id}")


def send_message(key, event):
    def error_message(text):
        bot.send_message(674796107, f'Итерация была прервана из-за ошибки: {text}')