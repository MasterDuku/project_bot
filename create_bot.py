from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv, find_dotenv
import os



load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)