from cgitb import text
import telebot
import datetime
import random

token = "5482925230:AAFtL0nSWzRO0OVQdTuFk6zzZa3uz4kBO2g"

bot = telebot.TeleBot(token)

HELP = """
/help - список доступных команд.
/add <00.00.0000> <Текст задачи> - добавить задачу
/show <00.00.0000>- напечатать все добавленные задачи
/random - случайная задача на сегодня
/exit - выход из программы"""
tasks={}
random_task =["Случайная задача 1","Случайная задача 2","Случайная задача 3","Случайная задача 4"]

def search(a, b):
  if a in tasks:
      tasks[a].append(b)
  else:
      tasks[a]=[b]

@bot.message_handler(commands=["show","print"])
def add(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text=""
    if date in tasks:
        text=date.upper()+"\n"
        for task in tasks[date]:
            text= text + "[]" + task + "\n"
    else:
        text="Задач на эту дату нет"
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=["random"])
def add(message):
    from datetime import datetime
    today=datetime.now().date()
    today1=str(today.day)+"."+str(today.month)+"."+str(today.year)
    rtask = random.choice(random_task)
    search(today1,rtask)
    text="Задача "+ rtask + " добавлена на дату "+ today1
    bot.send_message(message.chat.id, text) 

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date=command[1]
    task=command[2]
    search(date,task)
    text="Задача "+ task + " добавлена на дату "+ date
    bot.send_message(message.chat.id, text)  

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)    

#@bot.message_handler(content_types=["text"])
#def echo(message):
#    word=message.from_user.first_name
#    stri=str(message.text)
#    if word in stri:
#        bot.send_message(message.chat.id, "Куку")
#    else:
#        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)