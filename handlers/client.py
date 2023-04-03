
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot



# @dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет! Я бот и мнен интересно с тобой общаться.')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Test_my_project')

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, text='Иди туда, где вкусно пахнет,\nна улицу Космонавтов д.8')

# @dp.message_handler(commands=['working'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, text='Вс-Чт с 9:00 до 20:00, Пт-Сб с 9:00 до 23:00')



def register_heandlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_open_command, commands=['working'])