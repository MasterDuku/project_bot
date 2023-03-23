from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('--'*4,'Bot started', '--'*4)


@dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.text)





executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


print('--'*4, 'Отработал нормально', '--'*4)
