from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from config import TG_TOKEN

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)
