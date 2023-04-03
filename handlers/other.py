from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp
import json
from string import punctuation

# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply(text='Материться низя')
        await message.delete()

def register_heandlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)