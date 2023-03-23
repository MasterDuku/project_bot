from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


"""****************************Клиентская часть************************************"""
@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет! Я бот и мнен интересно с тобой общаться.')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Test_my_project')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, text='Иди туда, где вкусно пахнет,\nна улицу Космонавтов д.8')

@dp.message_handler(commands=['working'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, text='Вс-Чт с 9:00 до 20:00, Пт-Сб с 9:00 до 23:00')


"""****************************Админская часть************************************"""


async def on_startup(_):
    print('--'*4,'Bot started', '--'*4)

"""****************************Общая часть************************************"""
@dp.message_handler()
async def echo_send(message: types.Message):


    
    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)





executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


print('--'*4, 'Отработал нормально', '--'*4)
