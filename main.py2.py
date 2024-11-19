import telebot
# from telebot import types
# from telebot.storage import StateMemoryStorage

bot = telebot.TeleBot('7897812913:AAESbiz6ieAh4iORHFPfV7lhRNADMoBh0VA')

user_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, путник! Это наша бета-версия квестов, специально для технопарка. Мы представляем наш проект и хотим, чтобы сегодня вы его протестировали. Пройди три задания, и ты получишь небольшой приз 😉 \nВозможно, ты найдешь некоторые подсказки в нашем телеграм-канале: https://t.me/traektoria_40 \nА теперь напиши: <b>«<u>Поехали!</u>»</b> и получи первое задание!', parse_mode='html')
    user_state[message.chat.id] = 0

@bot.message_handler(func=lambda message: message.chat.id in user_state)
def handle_guest(message):
    current_state = user_state[message.chat.id]

    if current_state == 0 and message.text.lower() == 'поехали!' or message.text.lower() == 'поехали':
        bot.send_message(message.chat.id, 'Перед этим величественным зданием есть огромная надпись, которая гласит: «Мы вас любим и ждем!», она же написана и на ступеньках перед входом. \nУгадал, что за место? Тогда ищи его фотографию и ты узнаешь, что нужно сюда вписать, чтобы получить следующее задание. Удачи! 😉')
        user_state[message.chat.id] += 1

    elif current_state == 1 and message.text.lower() == 'огонь':
        bot.send_message(message.chat.id,'Поздравляю! Ты выполнил первое задание! \nКстати, интересный факт: наш драмтеатр был основан в 1777, но с тех пор три раза сгорал и несколько раз переносился в разные здания. \nНу что, идем дальше? Найди картинку с музеем космонавтики и ты, поймешь, что нужно вписать сюда. У тебя всё получится! :)')
        user_state[message.chat.id] += 1

    elif current_state == 2 and message.text.lower() == 'парк циолковского':
        bot.send_message(message.chat.id,'Молодец, это верный ответ! \nКстати, а ты знал, что рядом с Музеем Космонавтики стоит настоящий дублер ракеты Восток-1? Именно на ракете «Восток» Юрий Алексеевич Гагарин впервые полетел в космос. \nИтак, в твоей копилке уже два задания, осталось последнее. Ну что, поехали? \nНапиши ответ на этот вопрос: \nРаньше на месте Центрального парка культуры и отдыха стояла Калужская крепость, но она сгорела. Какой собор построили на месте старой церкви?')
        user_state[message.chat.id] += 1

    elif current_state == 3 and message.text.lower() == 'свято-троицкий собор' or message.text.lower() == 'свято-троицкий кафедральный собор' or message.text.lower() == 'троицский собор' or message.text.lower() == 'троицкий собор' or message.text.lower() == 'троицкий кафедральный собор':
        bot.send_message(message.chat.id,'Это верно, Свято-Троицкий Кафедральный собор был построен на месте старой деревянной церкви во имя Троицы Живоначальной, что была расположена в Калужской крепости, так же называемой Калужским Кремлем. \nА теперь… \nПоздравляю! 🥳 \nТы прошел наш квест, выполнив все задания! Подходи к стенду команды «Вектор успеха» за наградой! А еще там ты можешь получить новые интересные задания и увеличить свои награды 🎁 \n \nДо новых встреч!')
        del user_state[message.chat.id]

    else:
        bot.send_message(message.chat.id, 'Ox, кажется это неверный ответ... Пробуй снова!')



bot.polling(none_stop=True)

