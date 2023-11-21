import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

@dp.message_handler(commands="get_check")
async def bot_start(message: types.Message):
    await message.answer(f"Salom Api bot ishlamoqda, ishlatish uchun /dog shuni boshing {message.from_user.full_name}!")


@dp.message_handler(commands="dog")
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    api = 'https://dog.ceo/api/breeds/image/random'
    ansver = requests.get(api)
    rasm_manzili = ansver.json()['message']
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Bu bot ishlamoqda')

