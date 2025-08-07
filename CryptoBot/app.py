import telebot
from config import TOKEN, keys
from extensions import ConversionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = (
        'Здравствуйте! Я вам помогу узнать курс валют.\n'
        'Какая валюта вас интересует, введите сообщение формата:\n'
        '1. <имя валюты, цену которой хотите узнать>\n'
        '2. <имя валюты, цену в которой хотите узнать>\n'
        '3. <количество валюты>\n'
        'Пример:\n'
        'евро рубль 50\n\n'
        "Чтобы увидеть список всех доступных валют, используйте команду /values."
)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for key in keys.keys():
        text += f'- {key}\n'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')


         # Проверка, что введено ровно 3 значения
        if len(values) < 3:
            raise ConversionException('Вы не ввели все необходимые параметры: валюту отправителя, валюту получателя и количество.')
        elif len(values) > 3:
            raise ConversionException('Вы ввели лишние параметры. Пожалуйста, введите только: <валюта_отправитель> <валюта_получатель> <количество>.')

        quote, base, amount = values

        if quote not in keys:
            raise ConversionException(f'Валюта "{quote}" не найдена. Используйте /values для списка доступных валют.')
        if base not in keys:
            raise ConversionException(f'Валюта "{base}" не найдена. Используйте /values для списка доступных валют.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Некорректное число: "{amount}". Пожалуйста, введите числовое значение.')


        total_base = CryptoConverter.convert(quote, base, amount)
        total_price = total_base * amount

    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_price}'
        bot.send_message(message.chat.id, text)


bot.polling()