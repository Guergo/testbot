from cgitb import text
import telebot

token = "5482925230:AAFtL0nSWzRO0OVQdTuFk6zzZa3uz4kBO2g"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    word=message.from_user.first_name
    stri=str(message.text)
    if word in stri:
        bot.send_message(message.chat.id, "Куку")
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)