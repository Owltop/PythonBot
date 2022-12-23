import random

from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

import hashlib

TOKEN = '5810143707:AAGQq-c66N3LzP0L9SU3TT4OD9Xb5YffdmA'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

random_stickers = ['CAACAgIAAxkBAAEG3QNjndECAe4h2TAxXYSrnczTww2J_wACLBAAAvWLQUmTVj4wNGFSgSwE',
                   'CAACAgIAAxkBAAEG3QhjndG8GDsAATMd3vAhb9MeA2azq6MAAnEQAAJkkzlJbJXOIh9gboQsBA',
                   'CAACAgIAAxkBAAEG3QxjndHG3aNuGGUMvQABJ0NWNdoxPD8AAr4YAAL4HTFJW6CQdt9ywZksBA',
                   'CAACAgIAAxkBAAEG3Q5jndHWzSvm9IQPyvpDigVj0lpSTQAC5hAAAijRAUkerwi9D1QAAe4sBA',
                   'CAACAgIAAxkBAAEG3RBjndHZ0dX1TsPc10bCDD2NRiSJbgACViMAAiTiuUl3YUJo5EZqfCwE',
                   'CAACAgIAAxkBAAEG3RJjndHeDe9AEi7W3ST8TvqQ4xtRpAACfxQAAlML2EjmP7iruvyOOywE']

tomas = ['CAACAgIAAxkBAAEG3VpjndzH9eMEqSGv1iqesGVSTL-WHAACvx4AAppdMUnjZmzdaxMdNSwE',
         'CAACAgIAAxkBAAEG3VxjndzX89OUwKkmVU7rRjFgeUcT2QACPxYAAqAZ6Ut8sZhXFi6djSwE',
         'CAACAgIAAxkBAAEG3V5jndzZTlT4G_I3EiVAxNNenz_n-gAC4BIAAgMg6Uu9aWDjT5Mh7iwE']


def RandomSticker():
    return random.choice(random_stickers)


def RandomStickerTomas():
    return random.choice(tomas)


def RandomPercentage():
    return random.randint(0, 100)


@dp.message_handler(commands=['start'])
async def hello_message(message):
    await bot.send_message(message.chat.id,
                           "Этот бот, который измеряет веро-ть сдать акос и умеет делать другие прикольные вещи")
    await bot.send_message(message.chat.id,
                           "Функции:\n"
                           "/sticker кинуть рандомный стикер\n"
                           "/caos - вер-ть сдать акос\n"
                           "/caos_grade  - предполгаемая оценка по акосу\n"
                           "/tomas - Томас\n"
                           "/anek - 1-й анек\n"
                           "/anek2 - 2-й анек\n"
                           "/secret - секрет)\n"
                           "/help - показать все функции\n")


@dp.message_handler(commands=['help'])
async def hello_message(message):
    await bot.send_message(message.chat.id,
                           "Функции:\n"
                           "/sticker кинуть рандомный стикер\n "
                           "/caos - вер-ть сдать акос\n"
                           "/caos_grade  - предполгаемая оценка по акосу\n"
                           "/tomas - Томас\n"
                           "/anek - 1-й анек\n"
                           "/anek2 - 2-й анек\n"
                           "/secret - секрет)\n"
                           "/help - показать все функции\n")


@dp.message_handler(commands=['sticker'])
async def hello_message(message):
    await bot.send_sticker(message.chat.id, RandomSticker())


@dp.message_handler(commands=['secret'])
async def hello_message(message):
    await bot.send_message(message.chat.id, 'Сидят два негра, один другого спрашивает: "Почему сидишь?"\n' +
                           'Другой отвечает: "Потому что чёрный"')


@dp.message_handler(commands=['caos'])
async def hello_message(message):
    a = RandomPercentage()
    await bot.send_message(message.chat.id, "Веро-ть сдать Акос равна " + str(a))


@dp.message_handler(commands=['caos_grade'])
async def hello_message(message):
    a = RandomPercentage() // 10
    await bot.send_message(message.chat.id, "Предполагаемая оценка по акосу " + str(a))


@dp.message_handler(commands=['tomas'])
async def hello_message(message):
    await bot.send_sticker(message.chat.id, RandomStickerTomas())


@dp.message_handler(commands=['anek'])
async def hello_message(message):
    await bot.send_message(message.chat.id, "Как бы называлась ОС, разработанная анимешниками?\n" +
                           "\n" +
                           "huesOS")


@dp.message_handler(commands=['anek2'])
async def hello_message(message):
    await bot.send_message(message.chat.id, "Греки, возможно, и изобрели секс, но итальянцы добавили в него женщин.")


executor.start_polling(dp)
